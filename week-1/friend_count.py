#write a function countFriends() that accepts a dictionary as an argument 
#and returns a new dictionary that includes a new key friends_count:

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


def countFriends(ramit) : #function countFriends accepts dict. as an argument
    
    ramit_copy = ramit.copy() #copies ramit for new dictionary
    
    if 'friends' in ramit_copy: #friends key should be in new dict.
        friends_count = sum('name' in friend for friend in ramit_copy['friends'])
       #new key value should be the number of names in the nested friend key on ramit dict. 
        ramit_copy['friends_count'] = friends_count #new key
        
    return ramit_copy
    
new_dict = countFriends(ramit) #define new dictionary and apply function

print(new_dict) #call 
