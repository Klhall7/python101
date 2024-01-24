#NOTE: "Python expression" print(dictionary[key]), use a loop for two requirements
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
        'name': 'Jasmine',
        'email': 'jasmine@yahoo.com',
        'interests': ['photography', 'tennis']
        },
        {
        'name': 'Jan',
        'email': 'jan@hotmail.com',
        'interests': ['movies', 'tv']
        }
    ]
}
print(ramit['email']) #Write a python expression that gets the email address of Ramit.

first_val = ramit.get('interests', '')[0]
print(first_val) #Write a python expression that gets the first of Ramit's interests.

email = ramit['friends'][0]['email']
print(email)  #Write a python expression that gets the email address of Jasmine.

jan_interest = ramit['friends'][1]['interests'][1] 
print(jan_interest)
#Write a python expression that gets the second of Jan's two interests.
