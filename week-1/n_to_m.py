#prompt user for start and end 

start = int(input("Start from: ")) 
end = int(input("End on: "))

while end < start: 
    print("End number must be greater than or equal to the start number.")
    #user has to enter a number that allows the loop to print
    end = int(input("End on: ")) 
    
while start <= end :  
    print (start)
    start = start +1
    #increments start by 1 until end is reached
