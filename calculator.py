from app import * 

def tip_calculator():
    tip_levels = {"Good" : .20, "Fair" : .15, "Poor" : .1}
    tip = 0.0
    total = 0.0
    total_rounded_cents = 0.0
    splitting = 0
    
    bill = total_input
    level = service_input
    

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
        