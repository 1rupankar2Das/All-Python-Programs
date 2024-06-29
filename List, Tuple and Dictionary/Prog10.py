L1=[1,3,5]
L2=[6,7,8]
print(L1+L2)

L1=[1,2,3]
L2=['A','B','C']
L3=[3.7,7.2]
L4=L1+L2+L3
print(L4)

L1=[1,2,3]
C=L1*3
print(C)

#Slicing the list:-
L1=[1,2,3,4,5,6,7,8,9,10]
L2=L1[3:-3]
print(L2)

L1=[1,2,3,4,5,6,7,8,9,10]
L2[1]=28
print(L2)

L1=[1,2,3,4,5,6,7,8]
L2=L1[3:30]
print(L2)

L1=[1,2,3,4,5,6,7,8]
L2=L1[-15:6]
print(L2)

L1=[1,2,3,4,5,6,7,8]
L2=L1[2:5]
print(L2)

L1=[1,2,3,4,5,6,7,8]
L2=L1[7:10]
print(L2)

L1=[1,2,3,4,5,6,7,8]
L2=L1[10:20]
print(L2)#->Return Empty List

L1=["abc","xyz","pqr"]
print(L1)

#Indexing:-
L1=[1,2,3,4,5,6,7,8,9,10]
L2=L1[0:7:2]
print(L2)

L1=[1,2,3,4,5,6,7,8,9,10]
L2=L1[0:7:3]
print(L2)

L1=[1,2,3,4,5,6,7,8,9,10]
L2=L1[::3]
print(L2)

L1=[1,2,3,4,5,6,7,8,9,10]
L2=L1[::-1]
print(L2)

L1=[1,2,3,4,5,6,7,8,9,10]
L2=L1[::-2]
print(L2)

#Using slices for list modification:-
L1=[1,2,3,4,5,6,7,8,9,10]
L1[0:2]=[10,20]
print(L1)

L1=[1,2,3,4,5,6,7,8,9,10]
L1[0:2]="a"
print(L1)

L1=[1,2,3,4,5,6,7,8,9,10]
L1[0:2]=["a","b"]
print(L1)

#Slicer:-
L1=[1,2,3]
print(L1)

L1=[1,2,3]
L1[2:]="604"
print(L1)

L1=[1,2,3]
L1[10:20]="abcd"
print(L1)

#Append:-
L1=[1,2,3]
L1.append(10)
print(L1)

L1=[1,2,3]
L1.append(10)
L1[2]=50
print(L1)

L1=[1,2,3]
del L1[2]
print(L1)

L1=[1,3,5,7,8,10,15]
del L1[2:4]
print(L1)

#POP method:-
L1=[1,2,3,4,5,6]
L1.pop()
print(L1)

L1=[1,2,3,4,5,6]
var1=L1.pop(0)
print(L1)

L1=[1,2,3,4,5,6]
var2=L1.pop(3)
print(L1)

#Index:-
L1=[13,18,11,16,18,14]
L1.index(18)
print(L1)

#Append:-
L1=['red','yellow','blue']
L1.append('green')
print(L1)

L1=[1,2,3]
L2=L1.append(L2)
print(L1)
