"""Main file that links all files together."""
"""
main.py
---------
Coordinates all classes: Student, Grade, Course, School.
Provides example usage for your school management system.
"""

from student import Student
from course import Course
from grade import Grade
from school import School
from datetime import date

def main():
    # -------------------------------
    # 1️⃣ Create a school
    # -------------------------------
    my_school = School("Greenwood High")

    # -------------------------------
    # 2️⃣ Create courses
    # -------------------------------
    math_course = Course("Mathematics", "Mr. Newton", "2026")
    history_course = Course("History", "Ms. Curie", "2026")

    # Add courses to school
    my_school.add_course(math_course)
    my_school.add_course(history_course)

    # -------------------------------
    # 3️⃣ Create students
    # -------------------------------
    alice = Student("Alice Johnson", "9th Grade")
    bob = Student("Bob Smith", "9th Grade")

    # -------------------------------
    # 4️⃣ Create grades
    # -------------------------------
    g1 = Grade("Mathematics", 15, 2, date(2026, 4, 7), "Exam")
    g2 = Grade("Mathematics", 12, 1, date(2026, 4, 15), "Coursework")
    g3 = Grade("History", 18, 2, date(2026, 4, 10), "Exam")
    g4 = Grade("History", 14, 1, date(2026, 4, 12), "Coursework")

    # -------------------------------
    # 5️⃣ Add grades to students
    # -------------------------------
    alice.add_grade(g1)
    alice.add_grade(g3)
    bob.add_grade(g2)
    bob.add_grade(g4)

    # -------------------------------
    # 6️⃣ Enroll students in courses
    # -------------------------------
    math_course.enroll(alice)
    math_course.enroll(bob)
    history_course.enroll(alice)
    history_course.enroll(bob)

    # -------------------------------
    # 7️⃣ Display reports
    # -------------------------------
    print("=== Individual Student Reports ===")
    print(alice.generate_report())
    print(bob.generate_report())

    print("\n=== Class Averages ===")
    print(f"{math_course.course_name} Average: {math_course.class_average():.2f}")
    print(f"{history_course.course_name} Average: {history_course.class_average():.2f}")

    print("\n=== Top Students in Math ===")
    for student in math_course.top_student(2):
        print(f"{student.name}: {student.calculate_average():.2f}")

    print("\n=== School Statistics ===")
    print(my_school.overall_statistics())

    # -------------------------------
    # 8️⃣ Save school data to JSON
    # -------------------------------
    my_school.save_to_json()
    print("\nSchool data saved to 'school.json'.")

    # -------------------------------
    # 9️⃣ Load school data from JSON
    # -------------------------------
    loaded_school = School("Temp Name")  # Temporary name
    loaded_school.load_to_json()
    print("\nLoaded school data:")
    print(loaded_school.overall_statistics())

    # Verify a loaded student
    loaded_student = loaded_school.find_student_accross_all_courses("Alice Johnson")
    if loaded_student:
        student_obj, student_course = loaded_student
        print("\nLoaded Student Report:")
        print(student_obj.generate_report())
    else:
        print("Student not found in loaded school data.")

if __name__ == "__main__":
    main()