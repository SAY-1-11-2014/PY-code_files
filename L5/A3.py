def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

num1 = int(input("enter number 1"))
num2 = int(input("enter number 2"))
print(f"SUM : {add(num1, num2)}")
print(f"DIFFERENCE : {subtract(num1, num2)}")
print(f"PRODUCT : {multiply(num1, num2)}")
print(f"QUOTIENT : {divide(num1, num2)}")