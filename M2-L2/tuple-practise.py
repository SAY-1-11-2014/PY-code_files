#tuple - immutable
t1 = ('hello', 3.4, 8, 6, 'Sam')
print(t1)
#indexing -> Positive and Negative
print(t1[0])
print(t1[-1])
#creating a nested tuple
t2 = ('hello', 3.4, 8, 6, 'Sam', [2,5,8], (9,23))
print(t2)
#accessing a value from nested tuple
print(t2[-1][-2])
print(t2[-2][-2])
print(t2[0:5])
t3 = (91,)
print(t2+t3)