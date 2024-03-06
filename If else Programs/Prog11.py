# Wap that input marks of a student and print the grade of the student 
marks=int(input("Enter marks:"))
if(marks>=90):
    print("Grade A")
elif(marks>=80):
    print("Grade B")
elif(marks>=60):
    print("Grade C")
elif(marks>=40):
    print("Grade Pass")
else:
    print("Fail")