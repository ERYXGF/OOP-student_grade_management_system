"""Contains the School class. That class is the top level container that
"englobes" all other classes."""

#Imports Course, Grade and Student to be used in the School class:
from student import Student
from course import Course
from grade import Grade
#Imports json to load and save the schools info:
import json
class School():
    """
    Contains the School class: top level container englobing Grade, Student and Course class.
    -Attributes:
    1) school name
    2) dictionnary of Course objects keyed by course name
    -Methods:
    1) add_course()
    2) remove_course()
    3) find_student_accross_all_courses(name) --> Searches for name accross all courses
    4) overall_statistics() --> print school wide performance data
    5) save_to_json()
    6) load_to_json()
    """
    def __init__(self, name):
        self.name = name
        self.list_of_courses = {}

    def add_course(self, course: Course):
        #Course validation:
        if not isinstance(course, Course):
            raise TypeError("Expected a Course object (class).")
        self.list_of_courses[course.course_name] = course

    def remove_course(self, course_name):
        self.list_of_courses.pop(course_name, None)

    def find_student_accross_all_courses(self, name):
        #Searches accross all courses
        for course in self.list_of_courses.values():
            #Searches accross the courses list of students:
            for student in course.student_list:
                #Checks the name is valid:
                if student.name == name:
                    return student, course
        return None

    def overall_statistics(self):
        total_students = sum(len(course) for course in self.list_of_courses.values())
        return f"Courses: {len(self.list_of_courses)}, Students: {total_students}"
    
    def save_to_json(self):
        data = {
            "name": self.name,
            "courses": {
                name: {
                    "teacher": course.teacher_name,
                    "year": course.year,
                    "students": [student.to_dict() for student in course.student_list]
                }
                for name, course in self.list_of_courses.items()
            }
        }

        with open("school.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def load_to_json(self):
        try:
            with open("school.json", "r", encoding="utf-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            return  # No file yet, do nothing

        # Reset current state
        self.name = data["name"]
        self.list_of_courses = {}

        max_id = 0  # Track highest student ID

        # Rebuild courses
        for course_name, course_data in data["courses"].items():
            course = Course(
                course_name,
                course_data["teacher"],
                course_data["year"]
            )

            # Rebuild students
            for s in course_data["students"]:
                student = Student(s["name"], s["year_level"])
                student.id = s["id"]

                # Track max ID
                if student.id > max_id:
                    max_id = student.id

                # Rebuild grades
                for g in s["grades"]:
                    grade = Grade(
                        g["subject_name"],
                        g["score"],
                        g["coefficient"],
                        g["date"],
                        g["assessment_type"]
                    )
                    student.add_grade(grade)

                # ⚠️ IMPORTANT: make sure this matches your Course class
                course.enroll(student)

            self.add_course(course)

        # Fix ID counter to avoid duplicates
        Student.id_counter = max_id + 1