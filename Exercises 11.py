#funtion to calculate library fine
def fine(days_overdue):
    base_charge = 0.5
    day_charge = 0.80 * day
    price = base_charge + day_charge
    max_charge = 30
    if price > max_charge:
        price = 30
    return price


#main Routine
day = int(input("how many days overdue?"))
print(f"you have a fine of ${fine(day):.2f}")
