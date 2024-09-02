def hello():
    global x #global x will be used
    x = 5
    print(f"The local x is {x}")
    print("Hello Harry")
x = 4
print(x)

print(f"The Gloal X is {x}")
hello()

print(f"The Gloal X is {x}")