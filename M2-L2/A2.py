#SETS
s1 = {1,2,2,8,8,67}
print(s1)
s1.add(10)
print(s1)

s2 = {2,8,8,56,345,89,1}

print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
