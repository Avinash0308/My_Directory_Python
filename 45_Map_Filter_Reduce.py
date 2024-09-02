# #MAP
# def cube(x):
#     return x*x*x
# print(cube(2))
# l = [1,2,4,6,4,3]
# # newl = []
# # print(l)
# # for i in l:
# #     newl.append(cube(i))
# # print(newl)
# # newl = list(map(cube,l))
# newl = list(map(lambda x: x**3,l))
# print(newl)

# #FILTER
# def filter_function(a):
#     return a>4
# # newnewl = list(filter(filter_function,l))
# newnewl = list(filter(lambda x: x>2,l))
# print(newnewl)

from functools import reduce

numbers = [1,2,3,4,5]

sum = reduce(lambda x,y:x+y,numbers)

print(sum)
