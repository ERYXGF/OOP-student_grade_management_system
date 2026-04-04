"""Contains only the Grade class. The Grade class represents a single
graded assesment.
grade.py

ATTRIBUTES: 
    - subject_name
    - score (0-20) 
    - coefficient 
    - date
    - assesment_type (exam/coursework/oral)

METHODS: 
    - weighted_score --> returns score multiplied by coefficient 
    - is_passing() --> returns True if score >= 10
    - __str__
"""

#Imports the custom exception for score:
from exceptions import InvalidScoreError

#Creates the Grade class:
class Grade():

    #ATTRIBUTES:
    def __init__(self, subject_name, score, coefficient, date, assessment_type):
        #Raises custom exception if score is invalid:
        if not 0 <= score <= 20:
            raise InvalidScoreError("Score must be between 0 and 20.")
        self.subject_name = subject_name
        self.score = score
        self.coefficient = coefficient
        self.date = date
        self.assessment_type = assessment_type

    #METHODS:
    def weighted_score(self):
        return self.score*self.coefficient

    def is_passing(self):
        return self.score >= 10
  
    def __str__(self):
        return f"{self.subject_name} | Score: {self.score} | Coeff: {self.coefficient} | Date: {self.date} |Type: {self.assessment_type}"
