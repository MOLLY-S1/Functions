#movie tickets
def main_routine():
    adult = 0
    student = 0
    child = 0
    gift = 0
    total = 0
    sold = 0

    ticket_wanted = input("would you like tickets (Y,N)?").upper()
    while ticket_wanted != "N":
        ticket = input("What type of tickets do you want,\n"
              "C for child tickets\n"
              "A for adult tickets\n"
              "S for student tickets\n"
              "G for gift vouchers\n"
                       ":").upper()
        amount = int(input("how many tickets? "))
        confirm = input("Confirm (Y,N)?").upper()

        if confirm == "Y":
            if ticket == "A":
                adult += amount
            elif ticket == "C":
                child += amount
            elif ticket == "S":
                student += amount
            else:
                gift += amount

            return(f" here is your total so far:\n"
                   f" {adult} = adult sales,\n"
                   f" {student} = student sales, \n"
                   f"{child} = child sales, \n"
                   f"{gift} = gift vouchers")
    while 

#main rountine
print(main_routine())

