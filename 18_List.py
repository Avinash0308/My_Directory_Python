marks = [1,3,2,"Bawaal Hai"]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
# print(marks[4])
print(len(marks))
if(4 in marks):
    print("Hai Bhai")
else:
    print("Nahi Hai Yaar")

print(len(marks)-3)
print(-3)
print(marks[-3])
print(marks[len(marks)-3])

print(marks)
print(marks[:])
print(marks[1:])
print(marks[1:-1])
print(marks[:-3])

# jump indexing
print(marks[0:4:2])
print(marks[4:0:-1])

lst = [i for i in range(4)]
print(lst)



listt = ["Kamaal Hai","Jai Ho","Ho gaya"]
lst = [items for items in listt if items]
print(lst)

lst = [items for items in listt if 'a' in items]
print (lst)