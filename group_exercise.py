
#convert procedural formatted dictionary to OOP
#personal benefit of OOP: easier to read
#other benefit: easier to remember and call methods in local scope unique to an object
    # v.s. using functions in ProForm that are global scope and affect all code
class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        
    def greet(self, person_2):
        print(" Hello %s, I am %s!" %(person_2.name , self.name))
        
    def print_contact_info(self):
        print("%s's email: %s " %(self.name, self.email)) 
        print("%s's phone: %s " %(self.name, self.phone))
        
sonny = Person(name ="Sonny", email="sonny@hotmail.com", phone= "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

sonny.greet(jordan)
jordan.greet(sonny)

sonny.print_contact_info()