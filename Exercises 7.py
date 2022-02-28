#funtion to print name a number of times
def print_name(name, number):
    for item in range(0, number):
        print(name)


#main Routine
user_name = input("what is your name? ")
user_name = user_name.upper()
user_number = int(input("how many times to be said: "))
print_name(user_name, user_number)
