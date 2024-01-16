print("Temperature Converter")
#user instructions/ title of code function
#have to use float because temperature is real number with a wide range
C = float(input("Temperature in C?: "))
#setup for user prompt, specifies they are starting with celsius
F = (C * 9/5) + 32
#formula for conversion
result= str(F) + " F" 
print(result)
# this code runs in python3 but cannot function is VS because 
#ValueError: could not convert string to float

