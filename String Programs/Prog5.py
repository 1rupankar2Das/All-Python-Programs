# Write a program to input a username, and a code(string) and determined whether a code is within the username. 
Uname=input("Enter User name: ") 
code=input("Enter code: ")
if code in Uname:
    print("code is in Username")
else:
    print("code is not in Username")