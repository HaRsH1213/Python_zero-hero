monthly_sales = [42, 38, 33, 38, 40, 45]
months = ['Jan', 'Feb', 'March', 'May', 'Jun', 'July']

threshold = 35

print("Without Using break Statement".center(100, "-"))
for sales_amount in monthly_sales:
    if sales_amount < 35:
        print(f"Sales amount {sales_amount} is less than the threshold")

    else:
        print(f"Sales amount {sales_amount} is greater than the threshold")\


print("Using the break Statement".center(100, '-'))


for sales_amount in monthly_sales:
    if sales_amount < threshold:
        print(f"Sales amount {sales_amount} is less than the threshold")
        break
    else:
        print(f"Sales amount {sales_amount} is greater than the threshold")


print("Using the break Statement with Sales amount along with its month".center(100, '-'))

for sales_amount, month in zip(monthly_sales, months):
    if sales_amount < threshold:
        print(f"Sales amount {sales_amount} is less than the threshold in a {month} month")
        break
    else:
        print(f"Sales amount {sales_amount} is greater than the threshold in a {month} month")