# Write a program that takes a list of tuples, each containing a student's 
# name and their score, and sorts the list by score in descending order.
def sort_students_by_score(students):
    sorted_students=sorted(students,key=lambda x: x[1],reverse=True)
    return sorted_students
students=[("Rahul",80),("Kabir",60),("Ranveer",99),("Bimal",89)]
sorted_students=sort_students_by_score(students)
print(sorted_students)