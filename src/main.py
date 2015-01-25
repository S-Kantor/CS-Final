##
# Name: David Landsman
# File name: main.py
# Description: Startup script used to setup database
##

import Login
from SQLWrapper import *

sqlWrapper = SQLWrapper()

# Create a table for students
sqlWrapper.createStudentsTable()

# Create a table for courses and fill it up with a list of courses
sqlWrapper.createCoursesTable()
sqlWrapper.generateCourses()

Login.main() # Start LoginFrame
