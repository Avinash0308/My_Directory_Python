l = [1, 3, 24, 5]
print(l)

l.append(7)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

l.sort(reverse=True)
print(l)

print(l.index(1))

l.append(1)
print(l)

print(l.index(1))

print(l.count(1))

print(l.count(23))

lisy = l
lisy[0] = 1

print(lisy)
print(l)

lisy = l.copy()
lisy[0] = 10

print(lisy)
print(l)

l.insert(1, 134)
print(l)

print(l)
l.pop()
print(l)

l.remove(1)
print(l)

l.remove(1)
print(l)

l.remove(l[0])
print(l)

'''l.remove(l[100])
print(l)'''

l.clear()
print(l)

m = [234, 23, 3]
print(m)

l.extend(m)
print(l)

l.extend(m)
print(l)

k = l + m
print(k)