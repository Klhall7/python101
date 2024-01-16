# Prompt the user for two things:
#The total bill amount
#The level of service, which can be one of the following: good, fair, or bad
#Calculate the tip amount and the total amount (bill amount + tip amount). 
# tip percentage based on the level of service is based on:
#good -> 20%, fair -> 15%, bad -> 10%
#Example session:
#user input: 100, good
#= Tip amount: $20.00 Total amount: $120.00

bill_amt = float(input("What is your bill amount? "))
service_lvl = input("How do you rate the level of service? ").lower()
#user prompt, with add on to make sure service level is lowercase 

tip_percent = {
    'good': 0.20, 'fair': 0.15, 'bad': 0.10 } #dictionary for service level

if service_lvl in tip_percent: 
    tip_calc = tip_percent[service_lvl]
    tip_amt = bill_amt * tip_calc 
    total_bill = bill_amt + tip_amt
    
    print("Tip Amount: $ %.2f" %tip_amt)
    print("Total Amount: $ %.2f" %total_bill)
    #float will only be 2 decimals 
    
else:
    print ("Invalid entry. Enter good, fair, or bad.")


