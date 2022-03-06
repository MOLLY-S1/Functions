#funtion to calculate gst
def calculate_gst(net_price):
    return net_price * 1.15



#main Routine
cost =  float(input("what is the price"))
print(f"Gst price is {calculate_gst(cost):.2f}")
