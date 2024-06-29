# Write a program that takes a tuple containing a person's name and 
# age, and unpacks it to print out a message stating the person's name 
# and age.
def print_person_info(person):
    name,age=person
    print(f"{name} is {age} years old")
person_info=("Rupankar",21)
print_person_info(person_info)