dic={
    "Harry":"Humar Being",
    "Spoon":"Object"
}
print(dic["Harry"])

ids = {
    344: "d",
    355: "e",
    366: "f"
}
print(ids[344])
print(ids)

#dictionaries are ordered

print(ids[366])
print(ids.get(366))

#if we try to directly use key to access it in dictionary, and if the key does not exist, an error will thrown
#but if we use .get() and key is not present, null will be returned "Harry Bhai is Jai Ho. Neeche try karta hoon, future avi kaisa hai bhai, tere se expectation hain"

print(ids.get(367))

#print(ids[367])

print(ids.keys())
print(ids.values())
print(ids.items())

for key in ids.keys():
    print(f"The value corresponding to key {key} is  {ids[key]}")

for key, value in ids.items():
    print(f"The value corresponding to key {key} is  {value}")