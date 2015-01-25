##
# Name: Aaron Nahum, Eytan Mezhibovsky, David Landsman
# File name: Selection.py
# Description: Contains UI code for the SelectionFrame
##

from tkinter import *
from SQLWrapper import *
from Timetable import *

sqlWrapper = SQLWrapper()

class SelectionFrame(Frame):
    def __init__(self, parent, studentId):
        '''Initializes a SelectionFrame.'''
        Frame.__init__(self, parent)

        self.parent = parent
        self.studentId = studentId
        self.selectedCourses = []

        self.initUI()

    def center_window(self):
        '''Centers the window on the screen.'''
        screenWidth = self.parent.winfo_screenwidth()
        screenHeight = self.parent.winfo_screenheight()

        # Calculate (x, y) position of window
        x = (screenWidth/2) - (650/2)
        y = (screenHeight/2) - (425/2)

        self.parent.geometry('%dx%d+%d+%d' % (650, 425, x, y))

    def initUI(self):
        '''Initializes the user interface by configuring the course listboxes and buttons.'''
        self.parent.title("Course Selection Screen")
        self.center_window()

        # Make the window resizable
        self.parent.resizable(width=TRUE, height=TRUE)

        # Selection title
        idLabel = Label(self, text="Select your courses:", font=(26))
        idLabel.grid(row=0, columnspan=20, column=0, sticky=S)

        # Selected courses title
        selectedCoursesLabel = Label(self, text="Selected Courses")
        selectedCoursesLabel.grid(row=1, column=2, sticky=S)

        # Scrollbar for selection courses listbox
        selectedCoursesScroller = Scrollbar(self, orient="vertical")
        # Selected courses listbox
        self.selectedCoursesBox = Listbox(self, width=30, height=20, yscrollcommand=selectedCoursesScroller.set)
        selectedCoursesScroller.config(command=self.selectedCoursesBox.yview)

        # Adjust positioning of selected courses listbox and scroller
        self.selectedCoursesBox.grid(row=2, column=2)
        selectedCoursesScroller.grid(sticky=E, row = 1, rowspan = 100, column = 3, ipady = 138)

        # Submit courses button
        submitButton = Button(self, text="Submit Courses", command = self.submitCourses)
        submitButton.grid(row=3, column=1)

        # Available courses title
        avaliableCoursesLabel = Label(self, text="Available Courses")
        avaliableCoursesLabel.grid(row=1, column=0, sticky=S)

        # Scrollbar for available courses listbox
        avaliableCoursesScroller = Scrollbar(self, orient="vertical")
        # Available courses listbox
        self.availableCoursesBox = Listbox(self, width=30, height=20, yscrollcommand=avaliableCoursesScroller.set)
        avaliableCoursesScroller.config(command=self.availableCoursesBox.yview)
        # Fill up the available courses listbox using courses from the courses table in the database
        for course in sqlWrapper.getAllCourses():
            self.availableCoursesBox.insert(END, course.name)

        # Adjust positioning of available courses listbox and scroller
        self.availableCoursesBox.grid(row=2, column=0)
        avaliableCoursesScroller.grid(sticky=E, row = 1, rowspan = 100, column = 0, ipady = 138, ipadx = 100)

        # Choose course button
        chooseButton = Button(self, text="Choose Course", command = self.chooseCourse)
        chooseButton.grid(row=3, column=0)

        # Remove course button
        removeButton = Button(self, text = "Remove Course", command = self.removeCourse)
        removeButton.grid(row = 3, column = 2)

        # Update the UI
        self.pack()

    def chooseCourse(self): #adds a course to your selected courses
        '''Called from chooseButton.
        Gets the selected course and adds it to the selected courses listbox.
        '''
        # Retrieve selection from available courses listbox
        selection = self.availableCoursesBox.get(self.availableCoursesBox.curselection()[0])

        # Check if course wasn't selected already
        if selection not in self.selectedCourses:
            # Check if selection is valid
            if len(selection) > 0:
                # Add to selection courses listbox
                self.selectedCoursesBox.insert(END, selection)
                self.selectedCourses.append(selection)

    def submitCourses(self): #submits the selected courses and stores it in the database
        '''Called from submitButton.
        Verifies if there are enough courses and calls ConfirmFrame.
        '''
        # Check if there are at least 6 courses
        if len(self.selectedCourses) >= 6:
            if messagebox.askyesno("Confirm", "Are you sure you want to select these courses?"):
                # Add selected courses
                sqlWrapper.addStudentCourses(self.studentId, self.selectedCourses)
                self.destroy()
                TimetableFrame(self.parent, self.studentId)
        else:
            messagebox.showinfo("Info", "Please select " + str((6 - len(self.selectedCourses))) + " more course(s)!")

    def removeCourse(self):
        '''Called from removeButton.
        Removes a course from the selected courses listbox.
        '''
        # Check if there is at least 1 course to remove
        if len(self.selectedCourses) >= 1:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.selectedCoursesBox.delete(ANCHOR)
            self.selectedCourses.remove(selection)
        
        
