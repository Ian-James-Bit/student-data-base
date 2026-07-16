import sqlite3
class assignments:
    #this class holds assignments table and methods
    def __init__(self, database="my_database.db"):
        #connect to database or creates if doesnt exist
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        #making table
        #assignment id in case same name, one to many with classes so we add class id
        sql_statement = """CREATE TABLE IF NOT EXISTS assignments (
                            Assignment_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Class_ID INTEGER,
                            Assignment_Name TEXT NOT NULL,
                            FOREIGN KEY(Class_ID) REFRENCES classes(Class_ID)
                        )"""
        self.cursor.execute(sql_statement)
        self.conn.commit()
"""
    def addAssignment(Assignment_Name, Class_ID):

    def removeAssignment(Assignment_ID):
        #rem assignment and related info

    def editAssignmentName(Assignment_ID,newAssignmentName):

    def editAssignmentClass(Assignmeent_ID, newClassID):

    def viewAssignments():
        #might split this up, view all assignments, for a specific class, for a specific student
    
    def report(Assignment_ID):
    #given assignment show students who have it, grades of it for the students, and avg grade
"""