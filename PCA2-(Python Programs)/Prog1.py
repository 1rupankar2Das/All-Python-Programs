#Write a python program that input a string and print the string in reverse order.
def reverse(s):
    str=""
    for i in s:
        str=i+str
    return str 
s="Rupankardas"
print("The original string is: ",end="")
print(s)
print("The reversed string(using loops) is: ",end="")
print(reverse(s))
 