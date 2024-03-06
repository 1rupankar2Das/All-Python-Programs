#WAP that takes a string input and performs 
#various manipulations, such as converting it to uppercase, lowercase, 
#and title case, and also replacing certain characters with others based 
#on user input.
str1="Rupankar Das"
newStr=""
for i in range(0,len(str1)):
    if str1[i].islower():
        newStr+=str1[i].upper()
    elif str1[i].isupper():
        newStr+=str1[i].lower()
    else:
        newStr+=str1[i]
        print("String after case conversion: "+newStr)