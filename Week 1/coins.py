#Write a program that will prompt you for how many coins you want. Initially you have no coins. 
#It will ask you if you want a coin? If you type "yes", it will give you one coin
#print out the current tally. If you type no, it will stop the program. Example run:
# ("Tip Amount: $ %.2d" %tip_amt)
start = 0

while True:
    want_more = input("You have %s coins. Do you want another?(yes/no)".lower() % start ) #user input 
    if want_more == "yes":
        start += 1   
    elif want_more == "no":
        break
    else:
        print("Invalid entry. Must enter yes or no.") #user has to enter valid inputs
        
print("you now have %s .Bye" % start)

