class Student:

    def __init__(self, studentId, grade, selectedCourses, availableCourses, passwordHash):
        self.studentId = studentId
        self.grade = grade
        self.selectedCourses = selectedCourses
        self.availableCourses = availableCourses
        self.passwordHash = passwordHash
