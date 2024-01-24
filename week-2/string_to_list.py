string = "birthday" #create a string w/ at least 6 char
list = [] #make an empty list

for letter in string: #loop through string
    letter.isalpha() #only loop letters 
    
    add_list = list.append(letter) 
    #function to add loop letters to list
orig_list =list.copy()
print(orig_list) #check 

list.reverse() #reverse list
rev_list = list  #var assigns reversed list

print(rev_list) #check

new_string = "" #new variable; empty string

for char in rev_list: #loop through rev list
    char.isalpha() #only loop letters
    
    add_string= new_string + "".join(rev_list) #add loop char to new string
# .join() concatenates list elements, "" separates empty char (" ,) from list
print(add_string)
    
    
    
 


    
    
        