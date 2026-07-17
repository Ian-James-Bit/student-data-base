import sqlite3
class Students:
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

    def addStudent(self,Student_Name):
        self.cursor.execute("INSERT INTO students (Student_Name) VALUES(?)",(Student_Name,))
        self.conn.commit()
        

    def editStudents(self,Student_ID,Student_Name):
        self.cursor.execute("UPDATE students SET Student_Name = ? WHERE Student_ID =?",(Student_Name, Student_ID))
        self.conn.commit()
        print("Succefully changed")


    def removeStudent(self,Student_ID):
        query="DELETE FROM students WHERE Student_ID =?"
        self.cursor.execute(query,Student_ID)
        self.conn.commit()
        print("Succesfully removed.")

    def viewStudents(self):
        self.cursor.execute("SELECT * FROM students")
        data=self.cursor.fetchall()
        for row in data:
            print(row)
        
    def viewStudentByID(self,Student_ID: int):
        self.cursor.execute("SELECT * FROM students WHERE Student_ID = ?",(Student_ID,))
        row=self.cursor.fetchone()
        print(row)

    def viewStudentByName(self,Student_Name: str):
        self.cursor.execute("SELECT * FROM students WHERE Student_Name = ?",(Student_Name,))
        row=self.cursor.fetchone()
        print(row)
"""
    def report(Student_ID):
     #generate a report for a given student listing name, classes, assignments, grades, overall avg grade, avg/class
"""
