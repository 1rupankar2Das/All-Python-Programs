# Program to find largest number in a list in python.
def largest(list):
    large=list[0]
    for i in list:
        if i>large:
            large=i
    return large
list=[3,9,7,3,6,5,7,24,6]
print("largest in",list,"is")
print(largest(list))