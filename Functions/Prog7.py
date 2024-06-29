#Print factorial of a number recursively. 
def rec_factorial(n):
    if n==0:
        return 1
    else:
        return n*rec_factorial(n-1)
num=6
if num<0:
    print("Enter positive number: ")
elif num==0:
    print("Factorial of 0 is 1")
else:
    print("Factorial of",num,"=",rec_factorial(num))