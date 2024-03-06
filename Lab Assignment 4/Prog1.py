#WAP that that takes a list of numbers as input and performs 
#various operations such as finding the sum, average, maximum, 
#minimum, and sorting the list.
L=[4,5,1,2,9,7,10,8]
count=0
for i in L:
    count+=i
    avg=count/len(L)
    print("sum = ",count)
    print("average = ",avg)