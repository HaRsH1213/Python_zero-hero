for i in range(1,11):
    if i % 2 != 0:
        print(i)


print("Print odd number using continue".center(40,'-'))

for i in range(1,11):
    if i % 2 == 0:
        continue

    print(i)