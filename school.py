import sqlite3
from students import Students
import grades
import assignments
import classes

class School:

    def __init__(self):
        self.students=Students()
        # self.classes=classes()
        # self.assignments=assignments()
        # self.grades=grades()

    def menu(self):
        answer=input("Please select an option:\n    1.Student Menu\n    2.Class Menu\n    3.Assingments Menu\n    4.Grades Menu\n")
        if answer=="1":
            self.studentMenu()

    def studentMenu(self):
        answer=input("Please select an option:\n    1.Add Student\n    2.Edit Student\n    3.Remove Student\n    4.View Student(s)\n    5.Generate Student Report\n")
        if answer=="1":
            name=input("What is the name of the student you would like to add?\n")
            self.students.addStudent(name)
        elif answer=="2":
            id=input("What is the Student_ID of the student you would like to edit?")
            name=input("What would you like the new Student_Name to be?")
            self.students.editStudents(id,name)
        elif answer=="3":
            id=input("What is the Student_ID of the student you would like to remove?")
            self.students.removeStudent(id)
        elif answer=="4":
            answer=input("Please select an option:\n    1.View All Students\n    2.Search for a Student by Student_ID\n    3.Search for a Student by Name\n")
            if(answer=="1"):
                self.students.viewStudents()
            elif(answer=="2"):
                id=input("What is the Student_ID of the student you are searching for?")
                self.students.viewStudent(int(id))
            elif(answer=="3"):
                name=input("What is the Student_ID of the student you are searching for?")
                self.students.viewStudent(name)
            
    