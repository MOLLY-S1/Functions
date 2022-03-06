#movie tickets
def main_routine():
    adult = 0
    student = 0
    child = 0
    gift = 0
    total = 0
    sold = 0

    ticket_wanted = input("would you like tickets (Y,N)?")
    while ticket_wanted != "N":
        input("What type of tickets do you want,\n"
              "C for child tickets\n"
              "A for adult ")
