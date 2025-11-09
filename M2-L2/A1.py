 #tuples
'''
Perform the following operations on that tuple-

1. Create an empty tuple

2. Create a tuple with integer values

3. Create a tuple with mixed data type

4. Print any one element of that tuple

5. Create a nested tuple

6. Print any one element of that nested tuple

7. Perform slicing on that tuple

8. Illustrate Iteration through a tuple

9. Print updated tuple after each step
'''
#1
t1 = ()
print(t1)
#2
t2 = (1,2,3,4,5,6,7,8,9,0)
print(t2)
#3
t3 = ('sarthak', 'teacher', 'student', 10, 9, 2, 56)
print(t3)
#4
print(t3[2])
#5
t5 = (1,2,3,4,(123,456,789,102))
print(t5)
#6
print(t5[-1][-3])
#7
print(t3[1:5])
#8
for i in t2: 
    print(i)