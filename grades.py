import sqlite3
class grades:
    #this class holds grades table and methods
    def __init__(self, database="my_database.db"):
        #connect to database or creates if doesnt exist
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        #making table
        #although different a grade number can be the same on many student/assignments, the grade instance only has one assignment/student(like saying its Ian 1st test grade)
        #so its a one to many relationship, one student/assignment(assigned to many students) can have many grades
        sql_statement ="""CREATE TABLE IF NOT EXISTS grades (
                        Grade INTEGER,
                        Student_ID INTEGER,
                        Assignment_ID INTEGER,
                        FOREIGN KEY(Student_ID) REFRENCES students(Student_ID),
                        FOREIGN KEY(Assignment_ID) REFRENCES assignments(Assignment_ID)
                    )"""
        self.cursor.execute(sql_statement)
        self.conn.commit()
    """
    def addGrade(Student_ID,Assignment_ID,Grade):

    def removeGrade(Student_ID,Assignment_ID,Grade):

    def editGrade(Student_ID,Assignment_ID,newGrade):

    def viewAllGrades(Student_ID):

    def viewAssignmentGrades(AAssignment_ID):

    def viewClassGrades(Class_ID):
        #use a connecting table
    """
