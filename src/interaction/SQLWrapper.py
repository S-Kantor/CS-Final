import sqlite3

class SQLWrapper:

    def __init__(self, dbName = "timetable"):
        self.con = sqlite3.connect(dbName+'.db')
        self.cursor = self.con.cursor()

    def createStudentsTable(self):
        statement = "CREATE TABLE Students (studentId INTEGER, passwordHash TEXT, grade INTEGER, courses TEXT)"
        self.cursor.execute(statement)
        self.con.commit()
        
    def createCoursesTable(self):
        statement = "CREATE TABLE Courses (courseId INTEGER, name TEXT, priority INTEGER)"
        self.cursor.execute(statement)
        self.con.commit()

    def addStudent(self, studentId, passwordHash, grade):
        statement = "INSERT INTO Students VALUES (%s, '%s', %s)" % (studentId, passwordHash, grade)
        self.cursor.execute(statement)
        self.con.commit()

    def addStudentCourses (self, studentId, courses):
        statement = "UPDATE Students SET courses = '%s' WHERE studentId = %s" % (repr(courses), studentId)
        self.cursos.execute(statement)
        self.con.commit()
        
    def addCourse(self, courseId, name, priority):
        statement = "INSERT INTO Courses VALUES (%s, '%s', %s)" % (courseId, name, priority)
        self.cursor.execute(statement)
        self.con.commit()

    def deleteStudent(self, studentId):
        statement = "DELETE FROM Students WHERE studentId = %s" % (studentId)
        self.cursor.execute(statement)
        self.con.commit()
