#The reverse() method in Python reverses a list in-place
#Create a new variable called reversed_list & assign it reversed value of numbers
#use a separate line to reverse the list and then assign it to the new variable. 

numbers = [1, 2, 3, 4, 5, 99, 2600, 300] #list in-place

orig_list = numbers.copy() #copy numbers list to print

numbers.reverse() #reverse value of numbers 
reversed_list = numbers #create new variable assigns reversed value 

print(orig_list)  
print(reversed_list) 