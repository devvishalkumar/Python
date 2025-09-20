tup = (12,45,65,85,14,12,35,12,90)
print(tup)
print(tup[1])
print(tup[1:])
print(tup[:3])
print(tup[:])
print(tup.count(12))

new = list(tup)

new.append(50)
new.sort()
print(new)

tuple1 = tuple(new)
print(tuple1)

