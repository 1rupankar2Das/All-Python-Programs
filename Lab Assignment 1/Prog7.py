#WAP that calculates the grade of a student based 
#on their marks in a subject. Prompt the user to enter the marks 
#scored by the student and then display the corresponding grade 
#according to a predefined grading system.
print("Enter Marks Obtained in 5 Subjects: ")
total1 = 44
total2 = 67
total3 = 76
total4 = 99
total5 = 58 
tot = total1 + total2 + total3 + total4 + total4
avg = tot / 5 
if avg >= 91 and avg <= 100:
    print("Your Grade is A1")
elif avg >= 81 and avg < 91:
    print("Your Grade is A2")
elif avg >= 71 and avg < 81:
    print("Your Grade is B1")
elif avg >= 61 and avg < 71:
    print("Your Grade is B2")
elif avg >= 51 and avg < 61:
    print("Your Grade is C1")
elif avg >= 41 and avg < 51:
    print("Your Grade is C2")
elif avg >= 33 and avg < 41:
    print("Your Grade is D")
elif avg >= 21 and avg < 33:
    print("Your Grade is E1")
elif avg >= 0 and avg < 21:
    print("Your Grade is E2")
else:
    print("Invalid Input!")