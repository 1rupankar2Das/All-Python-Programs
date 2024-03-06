#WAP that checks whether a given number is 
#positive, negative, or zero. Prompt the user to enter a number and 
#then display whether it is positive, negative, or zero.
num=float(input("Input a number: "))
if num>0:
    print("It is a Positive number")
elif num==0:
    print("It is Zero")
else:
    print("It is a negative number")
