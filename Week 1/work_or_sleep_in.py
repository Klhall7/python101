print("Enter a number from 0 to 6 to find out if you work today")
#instructions for user
day = int(input('Day (0-6)? '))
#prompt user to enter day number 
if 1 <= day <= 5:
  print("Go to work!")
else:
  print("Sleep in")
# day 0 and 6 are weekends, day 1-5 are weekdays 