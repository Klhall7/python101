#Write a function that accepts two arguments: a name and a subject.
# return a string with name & subject interpolated in
#provide default arguments in case one or both are omitted

def madlib (name = "" , subject = ""): #accepts arguments
    return f"{name}'s favorite subject is {subject}." #f-string interpolated
 
print (madlib ("Jane", "Science")) 
#call and print function with default arguments