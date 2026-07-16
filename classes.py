import sqlite3
class classes:
    #this class holds classes table and methods
    def __init__(self, database="my_database.db"):
        #connect to database or creates if doesnt exist
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        #making table
        #class ID needed in case two class name are the same; many to many relationship with student need connecting table in school
        sql_statement = """CREATE TABLE IF NOT EXISTS classes (
                            Class_ID INTEGER,
                            Class_Name TEXT NOT NULL
                        )"""
        self.cursor.execute(sql_statement)
        self.conn.commit()

"""
    def addClass(Class_Name):

    def removeClass(Class_ID):
        #remove class and related info

    def editClassName(Class_ID,newClassName):
        
    def manageStudentEnrollment(Class_ID,Student_ID,Action):
        #add or remove student from class
    
    def viewClasses():
        #might split up into smaller functions, view all classes, view students in a class, view classes a student is enrolled in

    def report(Class_ID):      
        #given a class, shows studennts, assignments, class avg, highest and lowest grade
"""