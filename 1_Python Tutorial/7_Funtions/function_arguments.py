def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total


print("Total sum :", sum_all(1, 2, 3, 4, 5))



def company_info(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])

company_info(ticker = "AAPL", ceo = "Tim Cook", revenue = "200 billion", pe = 20, pb = 10.2)


print("Square of number".center(50,'-'))
def find_square(a):
    return a*a
print(find_square(5))

print("Square of number with lamda function".center(50,'-'))

x = lambda a: a**2

print(x(5))

print("Addition of number with lamda function".center(50,'-'))

x = lambda a ,b: a + b

print(x(5, 5))