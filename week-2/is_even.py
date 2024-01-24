#Write is_even function that accepts a number as an argument;returns a Boolean value. 
#Return True if the number is even; return False if it is not even.
num = int(input(" Enter a number: "))

def is_even(num): 
    
    if num %2 == 0: #checks if user num is even 
        return True
    print("Your number is even :)")
    
    else:
        return False
    print ("Your number is odd :(")
    
  
    
        
        