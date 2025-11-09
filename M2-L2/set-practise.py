#unique collection of values

s1 = {1,3,2,3,4,5,5}
print(s1)

s1.add(9)
print(s1)

#intersection
s2 = {2,3,5,6,7,8}
print(s1.intersection(s2))#common values in both sets
print(s1.union(s2))#common values + other values
print(s1.difference(s2))#ignores common values and gives remaining values from set 1 only
print(s1.symmetric_difference(s2))#remaining values from both sets