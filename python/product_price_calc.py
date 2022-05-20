no_items=int(input("Enter the number items: "))
tot_price=0
if (no_items < 10):
    tot_price=12*no_items
    print("Total cost: Rs.",tot_price)
elif (no_items >= 100):
    tot_price=7*no_items
    print("Total cost: Rs.",tot_price)
elif (no_items > 10)  or  (no_items < 99):
    tot_price=10*no_items
    print("Total cost: Rs.",tot_price)

