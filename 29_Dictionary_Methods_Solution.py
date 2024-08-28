ep1 = {
    122: 45,
    123: 89,
    670: 69,
    567: 69
}
ep2 = {
    222: 67,
    566: 90
}
ep1.update(ep2)
print(ep1)

for i,j in ep1.items():
    print(f"{i} , {j}")

# ep1.clear()
print(ep1)

empt = {}
print(empt)

ep1.pop(122)
print(ep1)

#.popitem() removes last in dict
ep1.popitem()

# del ep1

# print(ep1) error will occur

del ep1[222]
print(ep1)

