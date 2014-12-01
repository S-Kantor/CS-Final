import sqlite3
import Course
import Student

class SQLWrapper:

    def __init__(self):
        self.con = sqlite3.connect('test.db')
        self.cursor = self.con.cursor()

    def createStudentsTable(self):
        """
        Creates a table to store student data
        """
        statement = "CREATE TABLE Students (studentId INTEGER, passwordHash TEXT, grade INTEGER, courses TEXT)"
        self.cursor.execute(statement)
        self.con.commit()
        
    def createCoursesTable(self):
        """
        Creates a courses table
        """
        statement = "CREATE TABLE Courses (courseId INTEGER, name TEXT, priority INTEGER)"
        self.cursor.execute(statement)
        self.con.commit()

    def addStudent(self, studentId, passwordHash, grade, courses = None):
        """ (int, str, int) -> (none)

        Adds a student into the database
        """
        statement = "INSERT INTO Students VALUES (%s, '%s', %s, %s)" % (studentId, passwordHash, grade, repr(courses))
        self.cursor.execute(statement)
        self.con.commit()

    def addStudentCourses (self, studentId, courses):
        """ (int, str) -> (none)

        Adds all courses for Students to choose from
        """
        statement = "UPDATE Students SET courses = '%s' WHERE studentId = %s" % (repr(courses), studentId)
        self.cursos.execute(statement)
        self.con.commit()
        
    def addCourse(self, courseId, name, priority):
        """ (int, str, int) -> (none)

        Adds a course to the Students selected courses
        """
        statement = "INSERT INTO Courses VALUES (%s, '%s', %s)" % (courseId, name, priority)
        self.cursor.execute(statement)
        self.con.commit()

    def deleteStudent(self, studentId):
        """ (str) -> (none)

        Deletes a student from a selected course
        """
        statement = "DELETE FROM Students WHERE studentId = %s" % (studentId)
        self.cursor.execute(statement)
        self.con.commit()

    def getCourse(self, courseId):
        statement = "SELECT * FROM Courses WHERE courseId = %s" % (courseId)
        self.cursor.execute(statement)
        row = self.cursor.fetchone()
        return Course.Course(row[0], row[1], row[2])

    def getAllCourses(self):
        statement = "SELECT * FROM Courses"
        self.cursor.execute(statement)

    def getStudent(self, studentId):
        statement = "SELECT * FROM Students WHERE studentId = %s" % (studentId)
        self.cursor.execute(statement)
        row = self.cursor.fetchone()
        return Student.Student(row[0], row[1], row[2])

    def getAllStudents(self, studentId):
        statement = "SELECT * FROM Students"
        self.cursor.execute(statement)



