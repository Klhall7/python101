# Write a value_of_change function that accepts 2D tuple and 
#returns the calculation of the monetary value specified by the tuple.
#Brainstorm : break tuple into elements, calculate val of each element 

#make_change tuple from lvl 9000
tuple = (
(1, 0, 0, 0, 1, 0), #tuple[0]
(1, 0, 0, 2). #tuple[1]
) 

def value_of_change (tuple): 
# (*) extracts values to be passed as arguments
# define val of bills & coins
    bills_val = calc_bills(*tuple[0])
    coins_val = calc_coins(*tuple[1])
#calc total of bills and coins
    total_change = bills_val + coins_val
#print two decimal places
    return round (total_change , 2)

#break down values of bills & calculate $ total
def calc_bills(singles, fives, tens, twenties, fifties, hundreds):
    val_singles = singles * 1
    val_fives= fives * 5
    val_tens= tens * 10
    val_twenties= twenties * 20
    val_fifties= fifties * 50
    val_hundreds= hundreds * 100
#add up total of each bill
    result = sum([val_singles, val_fives, val_tens, val_twenties, val_fifties, val_hundreds])
    return result

#same for coins 
def calc_coins(pennies, nickels, dimes, quarters):
    val_pennies = pennies * .01
    val_nickels = nickels * .05
    val_dimes = dimes * .1
    val_quarters = quarters * .25
#add up total of each coin
    result = sum([val_pennies, val_nickels, val_dimes, val_quarters])
    return result



print (float(value_of_change(tuple))) #need float to print decimal



