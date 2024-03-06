#Develop a Python program that takes a string and a character as 
#input and counts the number of occurrences of that character in the 
#string.
count=0
my_string="Rupankar"
my_char="k"
for i in my_string:
    if i==my_char:
        count+=1
print(count)