import sqlite3
import students
import grades
import assignments
import classes

class school:
    def __init__(self):
        self.students=students.students()
        self.classes=classes.classes()
        self.assignments=assignments.assignments()
        self.grades=grades.grades()
    
    