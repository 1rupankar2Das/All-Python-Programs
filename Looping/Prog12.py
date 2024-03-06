#Program to find sum of the series S=1+x+x2+x3+xn
x=float(input("Enter value of x: "))
n=int(input("Enter power value: "))
s=0
for a in range(n+1):
    s+=x**a
    print("Sum of first",n,"terms:",s)