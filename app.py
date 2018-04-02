import tornado.ioloop
import tornado.web
import tornado.log
from calculator import *

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
    self.render_template("calculator.html", {})
    
  def post(self):
      total_input = self.get_body_argument('total')
      service_input = self.get_body_argument('service')
      split_input = self.get_body_argument('split')
      
      if total_input and service_input and split_input:
        self.redirect("/results")
        tip_calculator(total_input,service_input,split_input)
      
      else:
        error = "FILL OUT THE FORM"

class ResultsHandler(TemplateHandler):
  def get(self):
    self.set_header(
      'Cache-Control',
      'no-store, no-cache, must-revalidate, max-age=0')
    self.render_template("results.html", {})


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
  PORT = int('8888')
  app.listen(PORT)
  tornado.ioloop.IOLoop.current().start()
