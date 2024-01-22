class Vehicle: #create class
    def __init__(self, make, model, year): #initialize attributes
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self): #added to define method in Vehicle class
        print(car.make, car.model, car.year) 


car = Vehicle(make= "Honda" , model = "HR-V", year ="2020") 
#instantiated Vehicle class


print(car.make, car.model, car.year) 
#accessed attributes of car
   

car.print_info()
#used print_info method to output car info
        