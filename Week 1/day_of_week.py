print("Enter a number from 0 to 6 to represent a day of the week")
#instructions for user
day = int(input ("Day (0-6)?"))
#sets up prompt for user and ensures entry is converted to a number
if day == 0:
    print("Sunday")
elif day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
else:
    print("Invalid input. Please enter a number between 0 and 6.")
# if else sets up conditions for user's entry. final else condition redirects
#the user if they don't put in a number from zero to six. 