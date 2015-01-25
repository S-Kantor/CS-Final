###
# Programmers: David Landsman, Aaron Nahum
# File name: Student.py
# Description: Model class for a student (stores metadata for a student)
###

class Student:
    def __init__(self, studentId, grade, selectedCourses, password, finalCourses):
        '''(int, int, str, str, str) -> (Student)
        Initializes a student object.
        '''
        self.studentId = studentId
        self.grade = grade
        self.selectedCourses = selectedCourses
        self.password = password
        self.finalCourses = finalCourses
