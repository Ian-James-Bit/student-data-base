import sqlite3
from students import Students
import grades
import assignments
from classes import Classes

class School:

    def __init__(self, database="my_database.db"):
        self.students=Students()
        self.classes=Classes()
        # self.assignments=assignments()
        # self.grades=grades()
        #making connecting tables

        #first is connecting students and classes
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()
        sql_statement = """CREATE TABLE IF NOT EXISTS enrollments (
                            Student_ID INTEGER,
                            Class_ID INTEGER,
                            FOREIGN KEY (Student_ID) REFERENCES students (Student_ID) ON DELETE CASCADE,
                            FOREIGN KEY (Class_ID) REFERENCES classes (Class_ID) ON DELETE CASCADE
                        )""" 
        self.cursor.execute(sql_statement)
        self.conn.commit()

    #enrollment functions

    def manageStudentEnrollment(self,Class_ID,Student_ID,Action):
        if Action=="add":
            self.cursor.execute("INSERT INTO enrollments (Student_ID,Class_ID) VALUES(?,?)",(Student_ID,Class_ID))
            self.conn.commit()
        elif Action=="remove":
            self.cursor.execute("DELETE FROM enrollments WHERE Student_ID = ? AND Class_ID = ?",(Student_ID,Class_ID))
            self.conn.commit()
        
        
    def viewStudentsClasses(self,Student_ID):
        self.cursor.execute("SELECT Class_Name FROM enrollments INNER JOIN classes ON enrollments.Class_ID = classes.Class_ID WHERE Student_ID = ?",(Student_ID,))
        data=self.cursor.fetchall()
        for row in data:
            print(row)

    def viewStudentsInClass(self,Class_ID):
        self.cursor.execute("SELECT Student_Name FROM enrollments INNER JOIN students ON enrollments.Student_ID = students.Student_ID WHERE Class_ID = ?",(Class_ID,))
        data=self.cursor.fetchall()
        for row in data:
            print(row)

    # def report(Class_ID):      
    #     #given a class, shows studennts, assignments, class avg, highest and lowest grade

    #


    #Menu stuff
    def menu(self):
        while(True):
            answer=input("Please select an option:\n    1.Student Menu\n    2.Class Menu\n    3.Assingments Menu\n    4.Grades Menu\n    5.Exit\n")
            if answer=="5":
                break
            elif answer=="1":
                self.studentMenu()
            elif answer=="2":
                self.classMenu()

    def studentMenu(self):
        answer=input("Please select an option:\n    1.Add Student\n    2.Edit Student\n    3.Remove Student\n    4.View Student(s)\n    5.Generate Student Report\n")
        if answer=="1":
            name=input("What is the name of the Student you would like to add?\n")
            self.students.addStudent(name)
        elif answer=="2":
            id=input("What is the Student ID of the student you would like to edit? ")
            name=input("What would you like the new Student_Name to be?")
            self.students.editStudents(id,name)
        elif answer=="3":
            id=input("What is the Student ID of the student you would like to remove? ")
            self.students.removeStudent(id)
        elif answer=="4":
            answer=input("Please select an option:\n    1.View All Students\n    2.Search for a Student by Student_ID\n    3.Search for a Student by Name\n")
            if(answer=="1"):
                self.students.viewStudents()
            elif(answer=="2"):
                id=input("What is the Student_ID of the student you are searching for?")
                self.students.viewStudentByID(int(id))
            elif(answer=="3"):
                name=input("What is the Student_ID of the student you are searching for?")
                self.students.viewStudentByName(name)
            
    def classMenu(self):
        answer=input("Please select an option:\n    1.Add Class\n    2.Remove Class\n    3.Edit Class Name\n    4.Manage Class Enrollment\n    5.View Classes Info\n")
        if answer == "1":
            name=input("What is the Class Name of the class you would like to add? ")
            self.classes.addClass(name)
        elif answer =="3":
            id=input("What is the Class ID of the class's name you would like to edit? ")
            name=input("What would you like the new class name to be? ")
            self.classes.editClassName(id,name)
        elif answer =="4":
            action=input("Would you like to add or a remove a student from a class?")
            studentID=input("What is the Student_ID?")
            classID=input("What is the Class_ID?")
            self.manageStudentEnrollment(classID,studentID,action)
        elif answer=="5":
            answer=input("Please select an option:\n    1.View Classes\n    2.View Student's Classes\n    3.View Classes's Students\n")
            if answer=="1":
                self.classes.viewClasses()
            if answer=="2":
                id=input("What is the Student_ID of the student whos classes you want to see? ")
                self.viewStudentsClasses(id)
            if answer=="3":
                id=input("What is the Class_ID of the class whos students you want to see? ")
                self.viewStudentsInClass(id)