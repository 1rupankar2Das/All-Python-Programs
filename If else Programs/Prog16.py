#WAP to Program to determine palindrome number
num=int(input("Enter a number: "))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
    if(temp==rev):
        print("The number is palindrome!")
    else:
        print("The number is not a Palindrome!")