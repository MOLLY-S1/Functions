def make_positive(number):
    new_value = abs(number)
    return new_value




#main routine
number_to_check = int(input("enter a number: "))
print(f"the absolute value of {number_to_check} is {make_positive(number_to_check)}")

