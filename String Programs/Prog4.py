# WAP program to input a series of digits and count a number of zero in that string 
num=input("Enter a number: ")
count=0
for i in num:
    if('0' in i):
        count+=1
    print("There is",count,"0 in",num)