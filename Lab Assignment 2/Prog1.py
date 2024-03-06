#WAP that takes a list of numbers as input and outputs the 
#sum of all the numbers in the list. Use a loop to iterate through the list 
#and accumulate the sum.
total=0
list1=[11,5,17,18,23]
for ele in range(0,len(list1)):
    total=total+list1[ele]
print("Sum of all elements in given list: ",total)