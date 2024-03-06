#WAP that prompts the user for an integer and then 
#calculates and prints the factorial of that number. Use a loop to 
#calculate the factorial.
num=10
factorial=1
if num<0:
    print("Sorry, factorial does not exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)