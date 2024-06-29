#Tuples:-
T1=(1,2,3,4,5)
print(T1)

#Empty Tuple:-
t1=(3,4,(7,10))
print(t1)

t2=tuple('hello')
print(t2)

L=['a','e','i','o','v']
t3=tuple(L)
print(t3)

#t1=tuple(input("Enter tuple elements: "))
#print(t1)

#t2=eval(input("Enter tuple elements: "))
#print("Tuple is: ",t2)

#Accessing tuple:-
#Length:-
T1=(1,2,3,4,5,3.7)
print(len(T1))

#Concatenation and Replication:-
t=(1,2,3)
a=t*3
print(a)

T1=('a','e','i','o','v')
a=T1[0]
b=T1[4]
c=T1[-1]
d=T1[-5]
print(a)
print(b)
print(c)
print(d)

T1=('abc','xyz','pqr','mnp')
for i in T1:
    print(i)

t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print(t3)



