#WAP that classifies a person's age into different 
#categories such as infant, child, teenager, adult, or senior citizen. 
#Prompt the user to enter their age and then display the 
#corresponding category.
age=int(input("Enter your age: "))
if age>=0 and age<=12:
    print("Your age group is Child")
elif age>=13 and age<=19:
    print("Your age group is Teenager")
elif age>=20 and age<=59:
    print("Your age group is Adult")
else:
    print("Your age group is Senior Citizen")