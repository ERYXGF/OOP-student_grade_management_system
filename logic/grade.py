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
#Creates the Grade class:
class Grade():

    #ATTRIBUTES:
    def __init__(self, subject_name, score, coefficient, date, assesment_type):
        self.subject_name = subject_name
        self.score = score
        self.coefficient = coefficient
        self.date = date
        self.assesment_type = assesment_type

    #METHODS:
    def weighted_score(self):
        return self.score*self.coefficient
    
    def is_passing(self):
        if self.score >= 10:
            return True
        else:
            return False
        
    def __str__(self):
        return (f"{self.subject_name}, {self.score}, {self.coefficient}, {self.date}, {self.assesment_type}")
        
        
    