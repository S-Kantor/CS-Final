##
# Programmer: Eytan Mezhibovsky, David Landsman, Aaron Nahum
# File Name: Timetable.py
# Description: Contains UI code for the TimetableFrame
##

from tkinter import *
from SQLWrapper import *

sqlWrapper = SQLWrapper()

class TimetableFrame(Frame):
    def __init__(self, parent, studentId):
        '''Initializes a TimetableFrame.'''
        Frame.__init__(self, parent)

        self.parent = parent

        self.studentId = studentId
        self.selectedCourses = eval(sqlWrapper.getStudent(self.studentId).selectedCourses)

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
        self.parent.title("Timetable Creation")
        self.centerWindow()
        self.pack(fill=BOTH, expand=1)

        # Configure table layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)

        # Timetable title
        idLabel = Label(self, text="Timetable", font=(26))
        idLabel.grid(row=0, columnspan=20, column=0, sticky=S)
        
        semster1 = Label(self, text="Semester 1:")
        semster1.grid(row=1, column=0, sticky=S)

        #Buttons for each period slot on the timetable
        self.sem1period1 = Button(self,text="Spare", command = self.selectPeriod1)
        self.sem1period1.grid(row=2, column=0)

        self.sem1period2 = Button(self,text="Spare", command = self.selectPeriod2)
        self.sem1period2.grid(row=3, column=0)

        self.sem1period3 = Button(self,text="Spare", command = self.selectPeriod3)
        self.sem1period3.grid(row=4, column=0)

        self.sem1period4 = Button(self,text="Spare", command = self.selectPeriod4)
        self.sem1period4.grid(row=5, column=0)

        self.sem1period5 = Button(self,text="Spare", command = self.selectPeriod5)
        self.sem1period5.grid(row=6, column=0)
        
        
        #####

        Box2ID = Label(self, text="Semester 2:")
        Box2ID.grid(row=1, column=1, sticky=S)

        self.sem2period1 = Button(self,text="Spare", command = self.selectPeriod6)
        self.sem2period1.grid(row=2, column=1)

        self.sem2period2 = Button(self,text="Spare", command = self.selectPeriod7)
        self.sem2period2.grid(row=3, column=1)

        self.sem2period3 = Button(self,text="Spare", command = self.selectPeriod8)
        self.sem2period3.grid(row=4, column=1)

        self.sem2period4 = Button(self,text="Spare", command = self.selectPeriod9)
        self.sem2period4.grid(row=5, column=1)

        self.sem2period5 = Button(self,text="Spare", command = self.selectPeriod10)
        self.sem2period5.grid(row=6, column=1)

        submitButton = Button(self, text="Submit", command = self.submitCourses)
        submitButton.grid(row=7, column=0, columnspan=2)
        
        #####
        selectedCoursesLabel = Label(self, text="Course List:")
        selectedCoursesLabel.grid(row=1, column=2, sticky=S)
        
        selectedCoursesScroller = Scrollbar(self, orient="vertical")
        self.selectedCoursesBox = Listbox(self, width=30, height=20, yscrollcommand=selectedCoursesScroller.set)
        selectedCoursesScroller.config(command=self.selectedCoursesBox.yview)

        self.selectedCoursesBox.grid(row=2, column=2, rowspan=5)
        selectedCoursesScroller.grid(sticky=E, row = 2, rowspan=5, column = 1, ipady = 138)

        for course in self.selectedCourses:
            self.selectedCoursesBox.insert(END, course)

    def removeFromListbox(self, selection):
        '''Removes the selected course from the listbox.'''
        self.selectedCourses.remove(selection)
        self.selectedCoursesBox.delete(ANCHOR)

    #functions to select where you want to put a course on the timetable
    def selectPeriod1(self):
        # If a period is not a spare, remove the class in that period
        if self.sem1period1["text"] != "Spare":
            selection = self.sem1period1["text"]
            self.selectedCoursesBox.insert(END, selection)
            self.sem1period1["text"] = "Spare"
            self.selectedCourses.append(selection)
        # Else, if a period is a spare, place the selected period in that class
        else:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.sem1period1["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod2(self):
        if self.sem1period2["text"] != "Spare":
            selection = self.sem1period2["text"]
            self.selectedCoursesBox.insert(END, selection)
            self.sem1period2["text"] = "Spare"
            self.selectedCourses.append(selection)
        else:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.sem1period2["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod3(self):
        if self.sem1period3["text"] != "Spare":
            selection = self.sem1period3["text"]
            self.selectedCoursesBox.insert(END, selection)
            self.sem1period3["text"] = "Spare"
            self.selectedCourses.append(selection)
        else:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.sem1period3["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod4(self):
        if self.sem1period4["text"] != "Spare":
            selection = self.sem1period4["text"]
            self.selectedCoursesBox.insert(END, selection)
            self.sem1period4["text"] = "Spare"
            self.selectedCourses.append(selection)
        else:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.sem1period4["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod5(self):
        if self.sem1period5["text"] != "Spare":
            selection = self.sem1period5["text"]
            self.selectedCoursesBox.insert(END, selection)
            self.sem1period5["text"] = "Spare"
            self.selectedCourses.append(selection)
        else:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.sem1period5["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod6(self):
        if self.sem2period1["text"] != "Spare":
            selection = self.sem2period1["text"]
            self.selectedCoursesBox.insert(END, selection)
            self.sem2period1["text"] = "Spare"
            self.selectedCourses.append(selection)
        else:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.sem2period1["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod7(self):
        if self.sem2period2["text"] != "Spare":
            selection = self.sem2period2["text"]
            self.selectedCoursesBox.insert(END, selection)
            self.sem2period2["text"] = "Spare"
            self.selectedCourses.append(selection)
        else:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.sem2period2["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod8(self):
        if self.sem2period3["text"] != "Spare":
            selection = self.sem2period3["text"]
            self.selectedCoursesBox.insert(END, selection)
            self.sem2period3["text"] = "Spare"
            self.selectedCourses.append(selection)
        else:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.sem2period3["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod9(self):
        if self.sem2period4["text"] != "Spare":
            selection = self.sem2period4["text"]
            self.selectedCoursesBox.insert(END, selection)
            self.sem2period4["text"] = "Spare"
            self.selectedCourses.append(selection)
        else:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.sem2period4["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod10(self):
        if self.sem2period5["text"] != "Spare":
            selection = self.sem2period5["text"]
            self.selectedCoursesBox.insert(END, selection)
            self.sem2period5["text"] = "Spare"
            self.selectedCourses.append(selection)
        else:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.sem2period5["text"] = selection
            self.removeFromListbox(selection)

    def submitCourses(self):
        '''Called from submitButton
        Stores the timetable in the database.
        '''
        self.finalCourses = [self.sem1period1["text"], self.sem1period2["text"], self.sem1period3["text"], self.sem1period4["text"], self.sem1period5["text"], self.sem2period1["text"], self.sem2period2["text"], self.sem2period3["text"], self.sem2period4["text"], self.sem2period5["text"]]
        # Make sure that the student placed all of his courses
        if len(self.selectedCourses) == 0:
            if messagebox.askyesno("Confirm", "Are you sure you want to submit this timetable?"):
                # Save the final courses in the database and close the program
                sqlWrapper.addFinalCourses(self.studentId, self.finalCourses)
                self.destroy()
                self.parent.destroy()
        else:
            messagebox.showerror("Error", "Cannot submit timetable without all courses.")
