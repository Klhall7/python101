#F = (C * 9/5) + 32 Write a function that takes a temperature
#in Celsius, converts it Fahrenheit, and returns the value.
C =  float(input("Temperature in Celsius?: ")) #user prompt
def c_to_f (C):
    F = (C * 9/5) 
    return round(F , 1) 
#round function (built-in)result to print only one decimal place

print (c_to_f (C)) #call func check

#C = (F - 32) * 5/9 write function that converts fahrenheit; return val
F = float(input("Temperature in Fahrenheit?: "))
def f_to_c (F):
    
    C = (F - 32) * 5/9 
    return round(C , 1)

print (f_to_c(F)) 