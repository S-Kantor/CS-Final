import sqlite3

class SQLWrapper:

    def __init__(self):
        self.con = sqlite3.connect('test.db')
        self.cursor = self.con.cursor()

    def createStudentsTable(self):
        """
        Creates a table where students can fill their table with courses
        """
        statement = "CREATE TABLE Students (studentId INTEGER, passwordHash TEXT, grade INTEGER, courses TEXT)"
        self.cursor.execute(statement)
        self.con.commit()
        
    def createCoursesTable(self):
        """
        Creates a table with all available courses
        """
        statement = "CREATE TABLE Courses (courseId INTEGER, name TEXT, priority INTEGER)"
        self.cursor.execute(statement)
        self.con.commit()

    def addStudent(self, studentId, passwordHash, grade):
        """
        Adds a student into the database
        """
        statement = "INSERT INTO Students VALUES (%s, '%s', %s)" % (studentId, passwordHash, grade)
        self.cursor.execute(statement)
        self.con.commit()

    def addStudentCourses (self, studentId, courses):
        """
        Adds a course to the Students selected courses
        """
        statement = "UPDATE Students SET courses = '%s' WHERE studentId = %s" % (repr(courses), studentId)
        self.cursos.execute(statement)
        self.con.commit()
        
    def addCourse(self, courseId, name, priority):
        statement = "INSERT INTO Courses VALUES (%s, '%s', %s)" % (courseId, name, priority)
        self.cursor.execute(statement)
        self.con.commit()

    def deleteStudent(self, studentId):
        """
        Deletes a student from a selected course
        """
        statement = "DELETE FROM Students WHERE studentId = %s" % (studentId)
        self.cursor.execute(statement)
        self.con.commit()

    def getCourse(self, courseId):
        statement = "SELECT * FROM Courses WHERE courseId = %s" % (courseId)
        self.cursor.execute(statement)

    def getAllCourses(self):
        statement = "SELECT * FROM Courses"
        self.cursor.execute(statement)

    def getStudent(self, studentId):
        statement = "SELECT * FROM Students WHERE studentId = %s" % (studentId)
        self.cursor.execute(statement)

    def getAllStudents(self, studentId):
        statement = "SELECT * FROM Students"
        self.cursor.execute(statement)



