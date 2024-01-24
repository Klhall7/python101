user_start= int(input("Enter a starting number: ")) #prompt user
user_end= int(input("Enter an ending number: "))


while user_start <= user_end: 
    print(user_start) #current val of user input
    user_start += 1 #increment by 1, inclusive
    if user_start > user_end : #end when current number matches the end 
        break
    
else:
    print("Invalid. Ending number must be greater than start number.")
    
