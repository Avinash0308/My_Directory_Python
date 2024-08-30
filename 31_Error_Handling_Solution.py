a = input("Enter the number: ")
print(f"Multiplication Table of {a} is: ")

try:
    for i in range (1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
    print("Invalid Input")

print("Some Important Lines of Code")
print("End of Program")

try:
    num = int(input("Enter the number: "))
    a = [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")
except IndexError:
    print("Index Error")
