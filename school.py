import sqlite3
from students import Students
import grades
import assignments
from classes import Classes

class School:

    def __init__(self):
        self.students=Students()
        self.classes=Classes()
        # self.assignments=assignments()
        # self.grades=grades()

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
        answer=input("Please select an option:\n    1.Add Class\n    2.Remove Class\n    3.Edit Class Name\n    4.Manage Class Enrollment\n    5.View Class(es)\n")
        if answer == "1":
            name=input("What is the Class Name of the class you would like to add? ")
            self.classes.addClass(name)
        elif answer =="3":
            id=input("What is the Class ID of the class's name you would like to edit? ")
            name=input("What would you like the new class name to be? ")
            self.classes.editClassName(id,name)
        elif answer=="5":
            answer=input("Please select an option:\n    1.View Classes\n    2.View Student's Classes\n    3.View Class'es Students\n    4.Manage Class Enrollment\n    5.View Class(es)\n")
            if answer=="1":
                self.classes.viewClasses()