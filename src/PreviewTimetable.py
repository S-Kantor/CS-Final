#########################################
# Programmers: Aaron Nahum, Eytan Mezhibovsky, David Landsman
# File Name: PreviewTimetable.py
# Description: Contains UI code for the PreviewTimetableFrame
#########################################

from tkinter import *
from SQLWrapper import *
from Timetable import *

sqlWrapper = SQLWrapper()

class PreviewTimetableFrame(Frame):
    def __init__(self, parent, studentId):
        '''Initializes a PreviewTimetableFrame.'''
        Frame.__init__(self, parent)

        self.parent = parent
        self.studentId = studentId

        # Retrieve the student using the given studentId
        self.student = sqlWrapper.getStudent(self.studentId)

        # Convert final courses to a list (they are stored as a string in the database)
        self.finalCourses = eval(self.student.finalCourses)

        self.initUI()
        
    def centerWindow(self):
        '''Centers the window on the screen.'''
        screenWidth = self.parent.winfo_screenwidth()
        screenHeight = self.parent.winfo_screenheight()

        # Calculate (x, y) position of window
        x = (screenWidth/2) - (650/2)
        y = (screenHeight/2) - (450/2)

        self.parent.geometry('%dx%d+%d+%d' % (650, 450, x, y))
        
    def initUI(self):
        '''Initializes the user interface by configuring the table layout, adding buttons, etc.'''
        self.parent.title("Timetable")
        self.centerWindow()
        self.pack(fill=BOTH, expand=1)

        # Configure table layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)

        # Timetable title
        idLabel = Label(self, text="Final Timetable", font=(26))
        idLabel.grid(row=0, columnspan=20, column=0, sticky=S)

        # Semester 1 title
        sem1Label = Label(self, text="Semester 1:")
        sem1Label.grid(row=1, column=0, sticky=S)

        # Non-functioning buttons for each period slot on the timetable
        self.sem1period1 = Button(self,text=self.finalCourses[0])
        self.sem1period1.grid(row=2, column=0)

        self.sem1period2 = Button(self,text=self.finalCourses[1])
        self.sem1period2.grid(row=3, column=0)

        self.sem1period3 = Button(self,text=self.finalCourses[2])
        self.sem1period3.grid(row=4, column=0)

        self.sem1period4 = Button(self,text=self.finalCourses[3])
        self.sem1period4.grid(row=5, column=0)

        self.sem1period5 = Button(self,text=self.finalCourses[4])
        self.sem1period5.grid(row=6, column=0)
        
        # Semester 2 title
        sem2Label = Label(self, text="Semester 2:")
        sem2Label.grid(row=1, column=1, sticky=S)

        self.sem2period1 = Button(self,text=self.finalCourses[5])
        self.sem2period1.grid(row=2, column=1)

        self.sem2period2 = Button(self,text=self.finalCourses[6])
        self.sem2period2.grid(row=3, column=1)

        self.sem2period3 = Button(self,text=self.finalCourses[7])
        self.sem2period3.grid(row=4, column=1)

        self.sem2period4 = Button(self,text=self.finalCourses[8])
        self.sem2period4.grid(row=5, column=1)

        self.sem2period5 = Button(self,text=self.finalCourses[9])
        self.sem2period5.grid(row=6, column=1)
