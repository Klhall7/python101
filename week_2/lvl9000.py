#functions will be global scope, parameters will be local

def make_change(total_charge, payment): #find the difference
    difference = round(payment - total_charge, 2)
#split difference into bills and coins
#convert diff to a string
    diff_as_string = str(difference)
    parts = diff_as_string.split(".")
#define bills and coins
    bills = parts[0]
#NOTE make the coins go to two decimal places
    coins = parts[1]
    return count_bills(bills), count_coins(coins)
           
def count_bills(payment_in_bills):
    payment_in_bills = int(payment_in_bills)
    hundreds = payment_in_bills // 100 #run bill check
    payment_in_bills %= 100 #update bill
    fifties = payment_in_bills // 50
    payment_in_bills %= 50
    twenties = payment_in_bills // 20
    payment_in_bills %= 20
    tens = payment_in_bills // 10
    payment_in_bills %= 10
    fives = payment_in_bills // 5
    payment_in_bills %= 5
    singles = payment_in_bills // 1
    payment_in_bills %= 1
    return (singles, fives, tens, twenties, fifties, hundreds)


def count_coins(payment_in_coins):
    payment_in_coins = int(payment_in_coins)
    quarters = payment_in_coins // 25
    payment_in_coins %= 25
    dimes = payment_in_coins // 10
    payment_in_coins %= 10
    nickels = payment_in_coins // 5
    payment_in_coins %= 5
    pennies = payment_in_coins // 1
    payment_in_coins %= 1
    return (pennies, nickels, dimes, quarters)

print(make_change(148.49, 200)) #check with defined arguments


