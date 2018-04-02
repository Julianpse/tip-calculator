from app import * 

def tip_calculator(total_input, service_input, split_input):
   
    tip_levels = {
        "Good" : .20, 
        "Fair" : .15, 
        "Poor" : .1
    }
    
    tip = 0.0
    total = 0.0

    bill =  float(total_input)
    level = service_input
    split = float(split_input)

    for levels, percent_tip in tip_levels.items():
        if level == levels: 
            tip = bill * percent_tip
            total = tip + bill
            
            #Rounds to 2 decimal places for cents
            total_rounded_tip = float("{0:.2f}".format(tip))
            total_rounded_cents = float("{0:.2f}".format(total))
            
            tip = total_rounded_tip
            total = total_rounded_cents
            split_price = total / split
            
            print("Tip amount: ${} \nTotal Bill: ${}\n Split {} way(s): {}".format(tip, total, split, split_price))
            
            
        
        