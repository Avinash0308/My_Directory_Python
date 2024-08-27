names = ("Avi","Me","chotu","Avinash","Tulsi","Khatbadan")

print(names)

temp = list(names)

temp.append("Avi0308")

temp.pop(1)

names = tuple(temp)
print(names)

caste = ("Agrawal","Nagvanshi")

full_name = names + caste
print(full_name)

tappu = (1,3,32,32,5,2,2,23)
print(tappu.count(3))
print(tappu.count(23))

print(tappu.index(3))
# print(tappu.index(234))
print(tappu.index(23,4,8)) #first value is number we want to know index of the next two numbers defines the index where the given number need to be searched

print(len(tappu))
