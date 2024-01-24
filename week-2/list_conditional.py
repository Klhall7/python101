tv_list = ['Bones', 'Booth', 'Angela', 'Jack'] 

name_check = 'Sweets' #check for name add


if name_check in tv_list:
    tv_list.remove(name_check) 
    
else:
    tv_list.append(name_check)
    
print(tv_list)

name_check_two = 'Bones' #check for name remove

if name_check_two in tv_list:
    tv_list.remove(name_check_two) 
    
else:
    tv_list.append(name_check_two)

print(tv_list)


    