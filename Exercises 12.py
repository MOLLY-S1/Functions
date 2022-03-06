#movie tickets program
def tickets(count):
    count = 0
    Adult = 15
    child = 10
    student = 12
    gift = 8

    Acount = 0
    c_count= 0
    scount = 0
    gcount = 0

while question == "Y":
    if ticket == "A":
            count = count + Adult
            Acount += Acount
    elif ticket == "C":
            count = count + child
            c_count += 1
    elif ticket == "S":
            count = count + student
            scount += 1
    else:
            count = count + gift
            gcount += 1

while question != "Y":
        print(tickets(count))


#main routine
question = input("Do you want to buy movie tickets? ")
question = question.upper()
ticket = input("what type of tickets do you want? ")
ticket = ticket.upper()
tickets(ticket)
print(f'your total cost for tickets is ${tickets(ticket)}\n'
      f'this was made of {tickets(Acount)}')
