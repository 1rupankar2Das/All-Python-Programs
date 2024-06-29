# WAP to create a dictionary containing name of the student and his/her SGPA of any number of students inputted by the user in python. 
def create_sgpa_dictionary():
    sgpa_dict = {}
    num_students = int(input("Enter the number of students: "))    
    for i in range(num_students):
        name = input("Enter the name of student {}: ".format(i+1))
        sgpa = float(input("Enter the SGPA of {}: ".format(name)))
        sgpa_dict[name] = sgpa        
    return sgpa_dict
student_sgpa_dict = create_sgpa_dictionary()
print("Student SGPA Dictionary:", student_sgpa_dict)