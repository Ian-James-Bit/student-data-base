import sqlite3
class students:
    #this class holds students table and methods
    def __init__(self, database="my_database.db"):
        #connect to database or creates if doesnt exist
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        #making table
        sql_statement = """CREATE TABLE IF NOT EXISTS students (
                            Student_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Student_Name TEXT NOT NULL
                        )"""
        self.cursor.execute(sql_statement)
        self.conn.commit()
"""
    def addStudent(Student_ID,Student_Name):

    def editStudents(Student_ID):  

    def removeStudent(Student_ID):

    def viewStudents():

    #search for a specific student, not sure how yet or by what
    def viewStudent():
    
    def report(Student_ID):
     #generate a report for a given student listing name, classes, assignments, grades, overall avg grade, avg/class
"""
