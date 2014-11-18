import sqlite3

class SQLWrapper:

    def __init__(self):
        self.con = sqlite3.connect('test.db')
        self.cursor = self.con.cursor()

    def createStudentsTable(self):
        statement = "CREATE TABLE Students (studentId INTEGER, passwordHash VARCHAR(50), grade INTEGER)"
        self.cursor.execute(statement)
        self.con.commit()
        
    def createCoursesTable(self):
        statement = "CREATE TABLE Courses (courseId INTEGER, name VARCHAR(50), priority INTEGER)"
        self.cursor.execute(statement)
        self.con.commit()

    def addStudent(self, studentId, passwordHash, grade):
        statement = "INSERT INTO Students VALUES (%s, '%s', %s)" % (studentId, passwordHash, grade)
        self.cursor.execute(statement)
        self.con.commit()

    def addCourse(self, courseId, name, priority):
        statement = "INSERT INTO Courses VALUES (%s, '%s', %s)" % (courseId, name, priority)
        self.cursor.execute(statement)
        self.con.commit()

    def deleteStudent(self, studentId):
        statement = "DELETE FROM Students WHERE studentId = %s" % (studentId)
        self.cursor.execute(statement)
        self.con.commit()
