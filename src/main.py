##
# File name: main.py
# Description: Startup script
##

from Login import main
from SQLWrapper import *

s = SQLWrapper()

s.createStudentsTable()
s.createCoursesTable()
s.generateCourses()

main() # Start LoginFrame
