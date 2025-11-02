def rec_fac(n):
    if n == 1:
        return n
    else:
        return n*rec_fac(n-1)
num = int(input("Enter a number"))
if num < 0:
    print("Please enter numbers >= 0")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print(f"the factorial of {num} is {rec_fac(num)}")