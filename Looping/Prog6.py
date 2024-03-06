#WAP the sum of square of each element using the while loop
num=sum=0
i=1
while(i<=5):
    num=int(input("Enter Number:"))
    sum=sum+(num**2)
    i=i+1
    print("Sum =",sum)