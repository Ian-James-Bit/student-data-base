import sqlite3
class data:
    #this class basically represents an instance of a school or somehting like that

    #making sure table stuff is all working
    def test(self):
        sql_statements = ["""CREATE TABLE IF NOT EXISTS students (
                            Student_ID INTEGER PRIMARY KEY,
                            Student_Name TEXT NOT NULL
                        )""",
                        
                        """CREATE TABLE IF NOT EXISTS classes (
                            Student_ID INTEGER PRIMARY KEY,
                            Class_Name TEXT NOT NULL
                        )""",
                        
                        """CREATE TABLE IF NOT EXISTS assignments (
                            Class_Name INTEGER PRIMARY KEY,
                            Assignment_Name TEXT NOT NULL
                        )""",
                        
                        """CREATE TABLE IF NOT EXISTS grades (
                            Student_ID INTEGER PRIMARY KEY,
                            Assignment_Name TEXT NOT NULL,
                            Grade INTEGER UNIQUE
                        )"""
        ]
        with sqlite3.connect('school.db') as conn:
            cursor = conn.cursor()

            for statement in sql_statements:
                cursor.execute(statement)

                conn.commit()
            sql= '''INSERT INTO students (Student_ID,Student_name)
                    VALUES(1,"Ian")'''
            
            cursor.execute(sql)
            conn.commit()
            cursor.execute('SELECT * FROM students')
            rows=cursor.fetchall()
            for row in rows:
                print(row)

    def __init__(self):
        pass