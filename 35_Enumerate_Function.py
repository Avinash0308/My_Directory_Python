a = [12,56,32,98,12,45,1,4]
# index = 0
# for mark in a:
#     print(mark)
#     if index == 3:
#         print(mark)
#     index += 1
for index, mark in enumerate(a):
    print(mark)
    if index == 3:
        print(mark)

for index, mark in enumerate(a,start = 2):
    print(mark)
    if index == 3:
        print(mark)