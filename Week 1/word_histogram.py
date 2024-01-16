#Write a word_histogram program that asks the user to input a sentence, and prints a dictionary 
#containing the tally of how many times each letter in the alphabet was used in the test.
def word_histogram(sentence):
    
    histogram = {} #creates empty dictionary 
    words = sentence.split() # Split the sentence into words
    
    for word in words: #iterate each word
        
        if word.isalpha(): #identifies input is made up of letters
            
            word = word.strip(".,!?\"'") #remove punctuation from the sentence
            
            word = word.lower() #convert word to lowercase for count
            
            if word in histogram:  #increment word count
                histogram[word] += 1
                
            else:
                histogram[word] = 1 
                
    return histogram

user_input= input("Please enter a sentence: ")

result = word_histogram(user_input) #calls histogram function to be applied to input

print(result) 