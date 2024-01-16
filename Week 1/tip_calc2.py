# add user option to split the bill 

bill_amt = float(input("What is your bill amount? "))
service_lvl = input("How do you rate the level of service? ").lower()
num_people = int(input("Split how many ways? "))
#user prompt, with add on to make sure service level is lowercase, add on for bill split

tip_percent = {
    'good': 0.20, 'fair': 0.15, 'bad': 0.10 } #dictionary for service level

if service_lvl in tip_percent and num_people >= 1: 
    tip_calc = tip_percent[service_lvl]
    tip_amt = bill_amt * tip_calc 
    total_bill = bill_amt + tip_amt
    amt_per_person = total_bill / num_people
    
    print("Tip Amount: $ %.2f" %tip_amt)
    print("Total Amount: $ %.2f" %total_bill)
    print("Amount Per Person: $ %.2f" %amt_per_person)
    #float will only be 2 decimals. amount per person integer had to be float to make sure change was displayed
    
else:
    print ("Invalid entry. Bill should be split by at least 1 person and the service level should be good, fair, or bad")
#user has to enter valid inputs. can't split 0 people
    
    
    
    
  



