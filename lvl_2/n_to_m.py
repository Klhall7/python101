#prompt user for start and end 

start = int(input("Start from: ")) 
end = int(input("End on: "))

while start <= end : #increments start by 1 until end is reached
    print (start)
    start = start +1
    
while end < start: #user has to enter a number that allows the loop to print 
    print("End number must be greater than or equal to the start number.")
    end_num = int(input("End on: "))