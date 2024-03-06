#Input multiple numbers and print their sum.
count=sum=0
ans='y'
while ans=='y':
    num=int(input("Enter number: "))
    if num<0:
        print("Number<0")
        break
    sum=sum+num
    count=count+1
    ans=input("Another number?(y/n)")
else:
    print("You entered",count,"numbers so far")
    print("Sum=",sum)

