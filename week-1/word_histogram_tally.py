#given word histogram tally
#print the top 3 words or letters.

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

sort_by_frequency = sorted(result.items(), key=lambda x: x[1], reverse=True)
print("The top three words are: ")
for word, count in sort_by_frequency:
    print(f"{word}:{count}")