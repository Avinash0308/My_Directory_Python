s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
print(s1,s2)
s1.update(s2)
print(s1,s2)

s1 = {1,2,3,4}
s2 = {7,6,5,4}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)

cities = {"Tokyo","Mad","Ber","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Mad"}
cities3 = cities.symmetric_difference(cities2)
print(cities,cities2,cities3)

city = cities.difference(cities2)
print(city)
cities2.difference_update(cities)
print(cities2)

print(cities.isdisjoint(cities2))

print(cities.issuperset(cities2))

print(cities2.issubset(cities))

cities.add("avi")
print(cities)

cities.remove("avi")
print(cities)

cities.add("avi")
print(cities)

cities.discard("avi")
print(cities)

item = cities.pop()
print(cities)
print(item)

del cities #delete set

cities2.clear() #delete all elements but not set
print(cities2)

