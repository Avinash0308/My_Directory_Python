a = 4
b = "4"

print(a is b) #exact location of object in memory
print(a == b) #value

x = [1,2,43] #mutable
y = [1,2,43]

print(x is y)
print(x == y)

x = 3 #immutable
y = 3
print(x is y)
print(x == y)

# constants have same memory.

x = (1,2) #tuple are immutable as well
y = (1,2)
print(x is y)
print(x == y)