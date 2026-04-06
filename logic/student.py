"""Contains only the student class. The class contains the students id
(randomly generated) and his notes, averages and everything."""

#Imports the grade class from grade.py
from grade import Grade

#Creates the student class:
class Student():
    """
    Contains all the students information:
    -Attributes:
    1) name
    2) Student id (generated using a class variable counter that increments with each new student)
    3) year level
    4) list of Grade objects (starting empty).
    -Methods:
    1) add_grade(grade) --> appends a Grade object
    2) calculate_average() --> computes the weighted average accross all grades
    3) get_grades_by_subject(subject) --> filters and returns grades for one subject 
    4) subject_average(subject) --> calculates the average for one subject
    5) best_subject() --> returns highest average
    6) worst_subject() --> returns lowest average 
    7) generate_report() --> prints a complete academic report card
    8) to_dict() --> converts to dictionary for future json serialisation
    9) __str__
    10) __repr__
    11) __len__ 
    """
    #Initializes empty id counter:
    id_counter = 1

    def __init__(self, name, year_level):
        self.name = name
        self.id = Student.id_counter
        Student.id_counter += 1
        self.year_level = year_level
        self.grades = []
 
    def add_grade(self, grade: Grade):
        self.grades.append(grade)

    def calculate_average(self):
        #If theres no grades yet:
        if not self.grades:
            return 0
        #Calculates the average:
        total_weighted = 0
        total_coefficients = 0

        for grade in self.grades:
            total_weighted += grade.weighted_score()
            total_coefficients += grade.coefficient

        if total_coefficients == 0:
            return 0
    
        return total_weighted / total_coefficients

    def get_grades_by_subject(self, subject):
        return [grade for grade in self.grades if grade.subject_name == subject ]

    def subject_average(self, subject):
        #Calculates the subject average:
        grades = self.get_grades_by_subject(subject)

        if not grades:
            return 0
        
        total_weighted = 0
        total_coefficients = 0

        for grade in grades:
            total_weighted += grade.weighted_score()
            total_coefficients += grade.coefficient

        if total_coefficients == 0:
            return 0

        return total_weighted / total_coefficients

    def best_subject(self):
        if not self.grades:
            return None
        
        subjects = set(grade.subject_name for grade in self.grades)
        return max(subjects, key=lambda subject: self.subject_average(subject)) 
    
    def worst_subject(self):
        if not self.grades:
            return None
        
        subjects = set(grade.subject_name for grade in self.grades)
        return min(subjects, key=lambda subject: self.subject_average(subject)) 

    def generate_report(self):
        if not self.grades:
            return f"{self.name} has no grades."

        report = f"Report for {self.name} (ID: {self.id})\n"
        report += f"Overall Average: {self.calculate_average():.2f}\n"

        subjects = set(grade.subject_name for grade in self.grades)
        for subject in subjects:
            avg = self.subject_average(subject)
            report += f"{subject}: {avg:.2f}\n"

        report += f"Best Subject: {self.best_subject()}\n"
        report += f"Worst Subject: {self.worst_subject()}\n"

        return report

    def to_dict(self):
         return {
            "name": self.name,
            "id": self.id,
            "year_level": self.year_level,
            "grades": [
                {
                    "subject_name": g.subject_name,
                    "score": g.score,
                    "coefficient": g.coefficient,
                    "date": g.date,
                    "assessment_type": g.assessment_type
                }
                for g in self.grades
            ]
        }

    def __str__(self):
         return f"{self.name} (ID: {self.id}) - Avg: {self.calculate_average():.2f}"

    def __len__(self):
        return len(self.grades)

    def __repr__(self):
        return f"Student(name={self.name}, id={self.id}, avg={self.calculate_average():.2f})"