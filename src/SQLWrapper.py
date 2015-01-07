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
        statement = "CREATE TABLE Students (studentId INTEGER, grade INTEGER, selectedCourses TEXT, availableCourses TEXT, passwordHash TEXT)"
        self.cursor.execute(statement)
        self.con.commit()
        
    def createCoursesTable(self):
        """
        Creates a courses table
        """
        statement = "CREATE TABLE Courses (courseId INTEGER, name TEXT, priority INTEGER)"
        self.cursor.execute(statement)
        self.con.commit()

    def addStudent(self, studentId, grade, passwordHash):
        """ (int, int, str) -> (none)

        Adds a student into the database
        """
        statement = "INSERT INTO Students VALUES (%s, %s, '%s', '%s', '%s')" % (studentId, grade, None, None, passwordHash)
        self.cursor.execute(statement)
        self.con.commit()
        

    def addStudentCourses (self, studentId, selectedCourses):
        """ (int, str) -> (none)

        Adds all courses for Students to choose from
        """
        statement = 'UPDATE Students SET selectedCourses = "%s" WHERE studentId = %s' % (repr(selectedCourses), studentId)
        print (statement)
        self.cursor.execute(statement)
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
        if row != None:
            return self.parseCourse(row)
        else:
            return None

    def getAllCourses(self):
        statement = "SELECT * FROM Courses"
        self.cursor.execute(statement)
        courses = []
        rows = self.cursor.fetchall()
        if rows == None:
            return None
        for row in rows:
            courses.append(self.parseCourse(row))
        return courses

    def getStudent(self, studentId):
        statement = "SELECT * FROM Students WHERE studentId = %s" % (studentId)
        self.cursor.execute(statement)
        row = self.cursor.fetchone()
        if row != None:
            return self.parseStudent(row)
        else:
            return None

    def getAllStudents(self):
        statement = "SELECT * FROM Students"
        self.cursor.execute(statement)
        students = []
        rows = self.cursor.fetchall()
        if rows == None:
            return None
        for row in rows:
            students.append(self.parseStudent(row))
        return students

    def parseStudent(self, row):
        return Student.Student(row[0], row[1], row[2], row[3], row[4])

    def parseCourse(self, row):
        return Course.Course(row[0], row[1], row[2])



