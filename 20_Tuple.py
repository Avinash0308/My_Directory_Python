tup = (1,5,6)
print(type(tup))
print(tup)

tup = (1)
print(type(tup))
print(tup)

tup = (1,)
print(type(tup))
print(tup)

# tup[0] = 100 It will give an error as values can't be changed

tup = (1,"Some thing new")
print(type(tup))
print(tup)

# tup.append(1) not possible in case of tuple

print(tup[0])
print(tup[1])

# else everything is quite similar to that of list like positive and negative indexing

tup = (1,3,3,3,3,3,3)
print(tup[0:4])
print(tup)

print(tup[0:100:2])


print(tup[0::3])

