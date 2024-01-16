#Write a letter_histogram program that asks the user for input, and prints a dictionary 
#containing the tally of how many times each letter in the alphabet was used in the word.
# write the function
# define a var that assigns the parameter
# initialize histogram (meaning dictionary, create var called histogram)
 
def letter_histogram(word):
    
    histogram = {} #creates empty dictionary 
    
    for letter in word:
        
        if letter.isalpha(): #check that input is made up of letters
            
            letter = letter.lower() #convert letter to lowercase for count
            
            if letter in histogram:  #increment letter count
                histogram[letter] += 1
                
            else:
                histogram[letter] = 1 #starts each new letter at 1 
    
                
    return histogram

user_input= input("Please enter a word: ")

result = letter_histogram(user_input) #calls histogram function to be applied to input

print(result)
    
    