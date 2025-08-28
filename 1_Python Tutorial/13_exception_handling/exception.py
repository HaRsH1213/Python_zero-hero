a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))

try:
    division = a/b
    #c = "abscf" + 45
    #print(division)
except ZeroDivisionError as ze:
    print("Exception error occurred :", ze)
    division=0
    #print(division)
except TypeError as te:
    print("Exception error occurred :",te)
    division = 0
    #print(division)

except Exception as e:
    print("Exception error occurred :", e)
    division = 0

print("Division is ",division)

try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
finally:
    if file:
        file.close()
    print("File closed.")


