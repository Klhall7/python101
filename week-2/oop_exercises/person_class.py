#given Class
class Person:
    def __init__(self, name, email, phone): 
      self.name = name
      self.email = email
      self.phone = phone
#constructor initialized instance object Person

    def greet(self, other_person):
      print('Hello %s, I am %s!' % (other_person.name, self.name))
    

sonny = Person(name = "Sonny", email = "sonny@hotmail.com", phone ="483-485-4948") 
    #instantiated Person class, defined values, stored in var 

jordan = Person(name ="Jordan", email="jordan@aol.com", phone="495-586-3456")

sonny.greet(other_person = jordan)
    #call greet method
jordan.greet(other_person = sonny)

print("Sonny's Contact info:" , sonny.email, sonny.phone)

print("Jordan's Contact info:" , jordan.email, jordan.phone)