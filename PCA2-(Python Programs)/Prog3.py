#Write a python program to find the factorial of a number using recursion.
def rec_factorial(n):
    if n==0:
        return 1
    else:
        return n*rec_factorial(n-1)
num=7
if num<0:
    print("Enter +ve number: ")
elif num==0:
    print("Factorial of 0 is 1")
else:
        print("Factorial of",num,"=",rec_factorial(num))

