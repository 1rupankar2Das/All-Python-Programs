#WAP  that finds the largest of three given 
#numbers. Prompt the user to enter three numbers and then display 
#the largest among them.
# Python program to find the largest number among the three input numbers
a = 10
b = 14
c = 12
if (a >= b) and (a >= c):
   largest = a
elif (b >= a) and (b >= c):
   largest = b
else:
   largest = c
print("The largest number is", largest)
