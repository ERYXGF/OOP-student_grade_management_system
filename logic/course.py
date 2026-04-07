"""
Only one class present: Course class.
Represents a a class/subject with an enrolled students list.
"""
#Imports the student class:
from student import Student
#Creates the course class:
class Course():
    """
    -Attributes:
    1) course name 
    2) teacher name
    3) year
    4) a list of Student objects
    -Methods:
    1) enroll(student)
    2) remove_student(student_id)
    3) class_average() --> calculates the mean of all students averages 
    4) top_student(n=3) that returns the 3 highest performing students
    5) failing_students() --> returns students with less than 10/20 average
    6) __len__ --> returns student count
    """
    def __init__(self, course_name, teacher_name, year):
        self.course_name = course_name
        self.teacher_name = teacher_name
        self.year = year
        self.student_list = []

    def enroll(self, student: Student):
        #If student is not from the correct class:
        if not isinstance(student, Student):
            raise TypeError("Expected a Student object (class).")
        #Appends the student:
        self.student_list.append(student)

    def remove_student(self, student_id):
        for student in self.student_list:
            #Checks student_id is valid:
            if student.id == student_id:
                #Removes the student:
                self.student_list.remove(student)
                return

    def class_average(self):
        #Checks there are students enrolled in the class:
        if not self.student_list:
            return 0
        #Calculates the class average:
        return sum(s.calculate_average() for s in self.student_list) / len(self.student_list)

    def top_student(self, n=3):
        #Returns the 3 top students:
        return sorted(
            self.student_list,
            key=lambda s: s.calculate_average(),
            reverse=True
        )[:n]

    def failing_students(self):
        #Returns the students with less than 10 average:
        return [
            student for student in self.student_list
            if student.calculate_average() < 10
        ]

    def __len__(self):
        #Returns the number of students enrolled in the class:
        return len(self.student_list)