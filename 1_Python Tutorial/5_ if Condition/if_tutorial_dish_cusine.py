indian = ["samosa", "daal", "naan"]
chinese = ["egg_role", "pot_sticker", "fried rice"]
italian = ["pizza", "pasta", "risotto"]

dish = input("Enter your dish: ")

if dish in indian:
    print(f'{dish} is an indian cuisine')
elif dish in chinese:
    print(f'{dish} is an chinese cuisine')
elif dish in italian:
    print(f'{dish} is an italian cuisine')
else:
    print("I don't know")



