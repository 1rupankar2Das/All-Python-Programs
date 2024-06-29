#Why is the following code not giving correct output even when 25 is a members of a dictionary
dic1={'age':25,'name':'xyz','Salary':23450.5}
val=dic1['age']
if val in dic1:
    print("This is member of the dictionary")
else:
    print("This is not a member of the dictionary")