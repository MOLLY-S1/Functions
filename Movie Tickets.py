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
        amount = globals(amount)
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

    while ticket_wanted != "Y":
        c_price = 7 * amount
        a_price = 12.50 * amount
        s_price = 9 * amount
        g_price = 0
        total = c_price + s_price + a_price

        if gift == 0:
            return(f" you total price for:\n"
           f"adult tickets is {a_price}\n"
           f"child tickets is {c_price}\n"
           f"student tickets is {s_price}\n"
           f"and your total is ${total}")

        else:
            return("because of gift vouchers your tickets are free")











#main rountine
print(main_routine())

