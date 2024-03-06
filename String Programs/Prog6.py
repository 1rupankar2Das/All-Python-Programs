# WAP a program to input a string and whether it is palindrome using string slicing
s=input("Enter a string: ")
if(s==s[::-1]):
    print(s,"is a palindrome")
else:
    print(s,"is not a palindrome")