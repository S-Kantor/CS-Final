##
# Name: Sam Kantor
# Date: 11/25/2014
# File: generateCourses.py
##



import SQLWrapper as wrapper

h = wrapper.SQLWrapper() # Initializing Class

h.createCoursesTable() # Create Course Table Function

Courses = ["English", "Math", "Comp Sci", "Entrepreneurship",
               "Accounting", "History", "Geography", "Music",
               "Religion"] #List of Courses

#Adds courses
i = 0
for i in range (0,2):
    h.addCourse(i + 1, Courses[i], 3)
for i in range (0,5):
    h.addCourse(i + 3, Courses[i+2], 2)
for i in range (0,2):
    h.addCourse(i+8, Courses[i+7],1)

    
    














        




