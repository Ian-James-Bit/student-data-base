import sqlite3
class Classes:
    #this class holds classes table and methods
    def __init__(self, database="my_database.db"):
        #connect to database or creates if doesnt exist
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        #making table
        #class ID needed in case two class name are the same; many to many relationship with student need connecting table in school
        sql_statement = """CREATE TABLE IF NOT EXISTS classes (
                            Class_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Class_Name TEXT NOT NULL
                        )"""
        self.cursor.execute(sql_statement)
        self.conn.commit()


    def addClass(self,Class_Name):
        self.cursor.execute("INSERT INTO classes (Class_Name) VALUES(?)",(Class_Name,))
        self.conn.commit()
    
    # def removeClass(self,Class_ID):
    #     #remove class and related info includes assignments grades ect
    

    def editClassName(self,Class_ID,newClassName):
        self.cursor.execute("UPDATE classes SET Class_Name = ? WHERE Class_ID =?",(newClassName,Class_ID))
        self.conn.commit()
    
    def viewClasses(self):
        self.cursor.execute("SELECT * FROM classes")
        data=self.cursor.fetchall()
        for row in data:
            print(row)

    
