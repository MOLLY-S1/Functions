def check_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"



#main Routine
get_bmi = float(input("Enter BMI:"))
print(f"with a bmi of {get_bmi} your status is {check_bmi(get_bmi)}")
