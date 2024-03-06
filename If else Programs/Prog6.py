#wap is take input of 3 number and find the smallest number 
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if(a<b and a<c):
    print("Smallest number is:"+str(a))
elif(b<a and b<c):
    print("Smallest number is:"+str(b))
else:
    print("Smallest number is:"+str(c))
