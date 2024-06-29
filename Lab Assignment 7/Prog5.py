# Design classes for students, courses, and instructors. Implement 
# functionalities for enrolling students in courses, assigning grades, and 
# generating transcripts.
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enroll_in_course(self, course):
        if course.course_id not in self.courses:
            self.courses[course.course_id] = {'course': course, 'grade': None}
            course.enroll_student(self)
            print(f"Student {self.name} enrolled in {course.title}.")
        else:
            print(f"Student {self.name} is already enrolled in {course.title}.")

    def assign_grade(self, course_id, grade):
        if course_id in self.courses:
            self.courses[course_id]['grade'] = grade
            print(f"Grade {grade} assigned to student {self.name} for course {self.courses[course_id]['course'].title}.")
        else:
            print(f"Student {self.name} is not enrolled in course with ID {course_id}.")

    def generate_transcript(self):
        transcript = f"Transcript for {self.name} (ID: {self.student_id}):\n"
        for course_info in self.courses.values():
            course = course_info['course']
            grade = course_info['grade']
            transcript += f"{course.title}: {'No grade assigned' if grade is None else grade}\n"
        print(transcript)
        return transcript

    def __str__(self):
        return f"Student(id={self.student_id}, name={self.name})"

class Course:
    def __init__(self, course_id, title):
        self.course_id = course_id
        self.title = title
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def __str__(self):
        return f"Course(id={self.course_id}, title={self.title})"

class Instructor:
    def __init__(self, instructor_id, name):
        self.instructor_id = instructor_id
        self.name = name
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"Instructor {self.name} is now teaching {course.title}.")

    def assign_grade(self, student, course_id, grade):
        if any(course.course_id == course_id for course in self.courses):
            student.assign_grade(course_id, grade)
        else:
            print(f"Instructor {self.name} does not teach course with ID {course_id}.")

    def __str__(self):
        return f"Instructor(id={self.instructor_id}, name={self.name})"

# Example usage
student1 = Student("S001", "Alice")
student2 = Student("S002", "Bob")

course1 = Course("C001", "Math 101")
course2 = Course("C002", "History 101")

instructor1 = Instructor("I001", "Dr. Smith")
instructor1.add_course(course1)
instructor1.add_course(course2)

# Enrolling students in courses
student1.enroll_in_course(course1)
student2.enroll_in_course(course1)
student1.enroll_in_course(course2)

# Assigning grades
instructor1.assign_grade(student1, "C001", "A")
instructor1.assign_grade(student2, "C001", "B")
instructor1.assign_grade(student1, "C002", "A-")

# Generating transcripts
student1.generate_transcript()
student2.generate_transcript()

