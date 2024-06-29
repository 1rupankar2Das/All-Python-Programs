T1=(1,2,3,4,5,6,7,8,9)
print(T1[-5:-2])

#Write a program to input a 4 element tuple and unpack it to 4 variables and recreate the tuple with elements swap as first element with third element and second element with the 4 element
t1=eval(input("Enter a 4 element tuple: "))
a,b,c,d=t1
print("Tuple unpacked in",a,b,c,d)
t1=a,b,c,d
print("Tuple after swapping elements: ",t1)

t1=(1,2,3,4)
print(len(t1))

t2=(10,15,20,25)
print(max(t2))

t3=("AB","CB","ZA","YC")
print(max(t3))

#t4=(1,2.5,"ABC")
#print(max(t4))

t5=(1,-1,3,2,1)
print(min(t5))

t3=("AB","CB","ZA","YC")
print(min(t3))

t1=(1,2,3,4)
print(sum(t1))

t1=(1,2,3,4)
a=t1.index(3)
print(a)

t6=(1,2,1,2,3,1,1,4,5)
a=t6.count(1)
print(a)

#Write a program that input a tuple of 7 elements find the minimum value and display the index number of that element.
#t1=eval(input("Enter 7 tuple elements: "))
#var1=min(t1)
#print("Min value",var1)
#print("Index no. is",t1.index(var1))

t1=(7,5,3,1,2)
s1=sorted(t1)
print("s1=",s1)

t2=(7,5,3,-1,2)
s1=sorted(t2, reverse=True)
print("s1=",s1)

t3=(11,'abc',(6,7,9,10,15))
print(len(t3))