###
# Programmers: David Landsman, Aaron Nahum
# File name: Course.py
# Description: Model class for a course (stores metadata for a course)
###

class Course:
    def __init__(self, courseId, name, priority):
        '''(int, str, int) -> (Course)
        Initializes a course object.
        '''
        self.courseId = courseId
        self.name = name
        self.priority = priority
