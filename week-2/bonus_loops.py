print("Given Range :  1, 2, 3 , 4 , 5, 6, 7, 8, 9, 10 ")
given_range = [1, 2, 3 , 4 , 5, 6, 7, 8, 9, 10]
user_start= int(input("Enter a starting number within the Given Range: "))
user_end= int(input("Enter an ending number within the Given Range: "))

if user_start and user_end in given_range:
    while user_start <= user_end: 
        print(user_start) #current val of user input
        user_start += 2 #increment by 2, inclusive
        if user_start > user_end : #end when current number > end, includes num 
            break
else: 
    print("Invalid Entry, input numbers within the Given Range.")
    
if user_start > user_end:
    print("Invalid. Ending number must be greater than start number.")
    
