#Nested Dictionaries 
emp={"John":{"age":24,"Salary":10000},"Sunil":{"age":25,"Salary":11000}}
for key in emp:
    print("Employee Name:",key)
    print("Age:",str(emp[key]['age']))
    print("Salary:",str(emp[key]['Salary']))