print("Please fill in the blanks below:")
print("_(name)_'s favorite way to reset is _(action)_.")
#setup for user to understand instructions
name = input("What is your name?: ").capitalize()
action = input("What activity or action helps you reset your mind?: ")
#defining inputs for user to fill in the blanks with. Name should be capital
madlib = "Coding is hard. " + str(name) + "'s favorite way to reset is by " + str(action) + "."
print(madlib)
# print will give sentence with the blanks filled in
