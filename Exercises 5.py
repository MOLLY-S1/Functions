def check_factor(num1, num2):
    if num1 % num2 == 0:
        return(f"{num2} is a factor of {num1} ")
    else:
        return(f"{num2} is not a factor of {num1}")


#main Routine
number1 = int(input("enter the bigger number"))
number2 = int(input("enter the smaller number"))
print(check_factor(number1, number2))
