import tornado.ioloop
import tornado.web
import tornado.log

from jinja2 import \
Environment, PackageLoader, select_autoescape

ENV = Environment(
  loader=PackageLoader('myapp', 'templates'),
  autoescape=select_autoescape(['html', 'xml'])
)

class TemplateHandler(tornado.web.RequestHandler):
  def render_template (self, tpl, context):
    template = ENV.get_template(tpl)
    context['page'] = self.request.path
    self.write(template.render(**context))

class MainHandler(TemplateHandler):
  def get(self):
    self.set_header(
      'Cache-Control',
      'no-store, no-cache, must-revalidate, max-age=0')
    self.render_template("base.html", {})
    
  def post(self):
      total = self.get_body_argument('total')
      service = self.get_body_argument('service')
      split = self.get_body_argument('split')
      
      if total and service and split:
          tip_calculator()

class ResultsHandler(TemplateHandler):
  def get(self):
    self.set_header(
      'Cache-Control',
      'no-store, no-cache, must-revalidate, max-age=0')
    self.render_template("results.html", {})


def tip_calculator():
    tip_levels = {"good" : .20, "fair" : .15, "bad" : .1}
    tip = 0.0
    total = 0.0
    total_rounded_cents = 0.0
    splitting = 0
    
    bill = float(input("Enter Total Bill Amount: "))
    level = input("Enter level of service(good, fair or bad): ")
    

    for levels, percent_tip in tip_levels.items():
        if level == levels: 
            tip = bill * percent_tip
            total = tip + bill
            
            #Rounds to 2 decimal places for cents
            total_rounded_tip = float("{0:.2f}".format(tip))
            total_rounded_cents = float("{0:.2f}".format(total))
            
            
            print("Tip amount: ${} \nTotal Bill: ${}".format(total_rounded_tip,total_rounded_cents))
            
    split = input("Are you splitting the bill today (yes/no)?: ").upper()
            
    if split == "YES":
        splitting = int(input("How many ways?: "))
        print("Each of you will pay: ${}".format(total_rounded_cents / splitting))
        
            
tip_calculator() 


def make_app():
  return tornado.web.Application([
    (r"/", MainHandler),
    (r"/results", ResultsHandler),
    (
      r"/static/(.*)",
      tornado.web.StaticFileHandler,
      {'path': 'static'}
    ),
  ], autoreload=True)
  
if __name__ == "__main__":
  tornado.log.enable_pretty_logging()
  
  app = make_app()
  PORT = int(os.environ.get('PORT', '8888'))
  app.listen(PORT)
  tornado.ioloop.IOLoop.current().start()
