#Implement a program that searches for a given element in a list and 
#returns the index if found, or a message if not found.
mylist=[]
print("Enter 5 elements for the list: ")
for i in range(5):
    val=int(input())
    mylist.append(val)
print("Enter an element to be search: ")
elem=int(input())
for i in range(5):
    if elem==mylist[i]:
        print("\nElement found at index:",i)
        print("Element found at Position:",i+1)