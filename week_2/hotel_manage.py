#given dictionary 
hotel = {
    '1': {
        '185': ['George Jefferson', 'Wheezy Jefferson'],
    },
    '2': {
        '237': ['Jack Torrance', 'Wendy Torrance'],
    },
    '3': {
        '333': ['Neo', 'Trinity', 'Morpheus']
    }
}

user_menu = input("Are you checking in or out today?: ").lower() 
#to do: #create % base on in or out 
#If checking in, ask for the number of occupants and what their names are.
#If checking out, remove the occupants from that room.

if user_menu == "in":
    occupants_in =input("How many people?: " )
    names_in =input("What is the name of each person?: " )
    new_occupants = []
    hotel.append (occupants_in: names_in) 
    
floor_num = input("What floor are you on?: ")
room_num = input("What is your room number: ")