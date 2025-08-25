expenses_rahul = [30, 40, 70, 90]
expenses_rohan = [40, 23, 10, 85]

print("Total expenses of both guys without using function".center(100, '-'))
total_expenses_rahul = 0
for expense in expenses_rahul:
    total_expenses_rahul += expense

print("Total rahul's expenses:", total_expenses_rahul)

total_expenses_rohan = 0
for expense in expenses_rohan:
    total_expenses_rohan += expense

print("Total rohan's expenses:", total_expenses_rohan)


print("Total expenses of both guys using function".center(100, '-'))

def total_expenses(expenses):
    """
    :param expenses: input list containing numbers
    :return: total sum of all numbers in the input list
    """
    total_exp = 0
    for expense in expenses:
        total_exp += expense

    return total_exp


print("Total rahul's expenses:", total_expenses(expenses_rahul))

print("Total rohan's expenses:", total_expenses(expenses_rohan))

print(help(total_expenses))
