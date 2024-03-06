# Wap to find the largest among 3 numbers in Python
a = int(input("Enter 1st Number:"))
b = int(input("Enter 2nd Number:"))
c = int(input("Enter 3rd Number:"))
if a > b and a > c:
    print(str(a) + "is the largest number.")
elif b > a and b > c:
    print(str(b) + "is the largest number.")
else:
    print(str(c) + "is the largest number.")