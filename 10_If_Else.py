a = int(input("What is your current wealth "))
print("Your current wealth is", a)

# conditional operators
# > , < , >= , <= ,==
print(a == 1000000)  # This will return boolean either true or false
print(a >= 1000000)
print(a <= 1000000)
print(a != 00)
if (a >= 1000000):  # In python the spaces are used to indentify the function or condition to which the code belong and if we try to add some extra spaces in the statements it will through an error
    print("You are really big shark")
elif (a == 9):
    print("Kuch Bhi")
else:
    # Upto the point the gap is manintained in the given code it will fall under some if else statement or we can say that this if used to remove the functionality of braces which is used in c and c++
    print("You need to improve a little bit")
    # This spaces are called indentations and they tell about the curly braces which is used in c and c++
    print("NO NO NO")
print("I will print always")

weight = int(input("Please enter your weight "))
print("You have entered your weight as",weight)
if(weight > 50):
    print("Your weight is too much you need to reduce it\n")
elif(weight>=30 and weight<=50):
    print("You have a perfect weight you can go with it\n")
else:
    print("You are under weight please incerease it\n")