# Write a program to input a integer number and check if it contains any zero in it
n=int(input("Enter a number: "))
s=str(n)
if '0' in s:
    print("There's a 0 in",n)
else:
    print("No 0 in",n)
