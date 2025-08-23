expenses = [1200, 1300, 1500, 1700]

total_expense = 0

for expense in expenses:
    total_expense = total_expense + expense

print(total_expense)


print("Month by Month expenses")

total_expense_new = 0
for i in range(len(expenses)):
    expense = expenses[i]
    print(f"Month {i+1} expense: {expense}")
    total_expense_new += expense

print(f"Total: {total_expense_new}")


print("Month by Month expenses Using Enumerate Function")

total_expense_new_1 = 0
for i, expense in enumerate(expenses):
    print(f"Month {i+1} expense: {expense}")
    total_expense_new_1 += expense

print(f"Total:{total_expense_new_1}")
