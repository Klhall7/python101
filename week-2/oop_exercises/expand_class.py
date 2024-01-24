class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone
         self.friends = [] #initialize instance to an empty list within the constructor 
         self.greeting_count = 0 #initialize it to 0

    def greet(self, other_person):
         print('Hello %s, I am %s!' % (other_person.name, self.name))
         self.greeting_count += 1
#Add a print_contact_info method for instance of Person
    def print_contact_info(self): #added to define method in Vehicle class
        print("%s's email: %s " %(self.name, self.email)) #interpolation output
        print("%s's phone: %s " %(self.name, self.phone))
        
    def add_friend(self, friend_name):
        self.friends.append(friend_name) #add method
         
        
    def num_friends(self):
        return len(self.friends) #add method
    
    def show_greeting_count(self):
        print(self.greeting_count)
        
    def __str__(self):
        return 'Person: {} {} {}'.format(self.name, self.email, self.phone)

rob = Person (name= "Rob", email= "rob.serr@gmail.com", phone = "518-256-1543")

rob.print_contact_info() #test instance

john = Person (name = "john", email= "john@aol.com", phone= "518-123-4567")

rob.greet(other_person = john) #call greet method

rob.friends.append(john) #add a friend to a person using list's append method

result = len(rob.friends) #using the len function on friends attribute
print(result) #check 

rob.add_friend(john) #add friend with new method 

print(rob.num_friends()) #count friends with new method

rob.greet(john)
rob.show_greeting_count() #call method test

print(str(rob))






    
