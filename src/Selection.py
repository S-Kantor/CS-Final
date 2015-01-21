##
# Name: Sam Kantor
# Date: 11/17/2014
# Assignment: New Window
##


from tkinter import *
from SQLWrapper import *
from Timetable import *
s = SQLWrapper()
selected_courses = []

class SelectionFrame(Frame):
    def __init__(self, parent, studentId, app):
        Frame.__init__(self, parent)

        self.parent = parent
        self.app = app

        self.initUI()

        self.studentId = studentId

    def initUI(self):
        self.parent.geometry("650x425+400+200")
        self.parent.title("Course Selection Screen")
        self.parent.resizable(width=TRUE, height=TRUE)


        idLabel = Label(self, text="Course Selection:", font=(26))
        idLabel.grid(row=0, columnspan=20, column=0, sticky=S)

        #####
        
        selectedCoursesLabel = Label(self, text="Course:")
        selectedCoursesLabel.grid(row=1, column=2, sticky=S)
        
        selectedCoursesScroller = Scrollbar(self, orient="vertical")
        self.selectedCoursesBox = Listbox(self, width=30, height=20, yscrollcommand=selectedCoursesScroller.set)
        selectedCoursesScroller.config(command=self.selectedCoursesBox.yview)

        self.selectedCoursesBox.grid(row=2, column=2)
        selectedCoursesScroller.grid(sticky=E, row = 2, rowspan = 100, column = 3, ipady = 138)

        submitButton = Button(self, text="Submit Course", command = self.submitCourses)
        submitButton.grid(row=3, column=1)
        
        #####
        
        avaliableCoursesLabel = Label(self, text="Available Courses:")
        avaliableCoursesLabel.grid(row=1, column=0, sticky=S)
        
        avaliableCoursesScroller = Scrollbar(self, orient="vertical")
        self.availableCoursesBox = Listbox(self, width=30, height=20, yscrollcommand=avaliableCoursesScroller.set)
        avaliableCoursesScroller.config(command=self.availableCoursesBox.yview)
        for course in s.getAllCourses():
            self.availableCoursesBox.insert(END, course.name)

        self.availableCoursesBox.grid(row=2, column=0)
        avaliableCoursesScroller.grid(sticky=E, row = 2, rowspan = 100, column = 1, ipady = 138)

        chooseButton = Button(self, text="Choose Course", command = self.chooseCourse)
        chooseButton.grid(row=3, column=0)
        
        #####

        removeButton = Button(self, text = "Remove Course", command = self.removeCourse)
        removeButton.grid(row = 3, column = 2)

        #####

        self.pack()

    def chooseCourse(self):
        selection = self.availableCoursesBox.get(self.availableCoursesBox.curselection()[0]) # get selected string
        if selection not in selected_courses:           
            if len(selection) > 0:
                self.selectedCoursesBox.insert(END, selection)
                selected_courses.append(selection)

    def submitCourses(self):
        if len(selected_courses) >= 6:
            self.newWindow = Toplevel(self.master)
            self.app = ConfirmFrame(self.newWindow, self.studentId)
            return
        else:
            print("Please select " + str((6 - len(selected_courses))) + " more course(s)")

    def removeCourse(self):
        if len(selected_courses) >= 1 and len(selected_courses) <= 6:
            selection = self.selectedCoursesBox.get(self.selectedCoursesBox.curselection()[0])
            self.selectedCoursesBox.delete(ANCHOR)
            selected_courses.remove(selection)
        else:
            return
        

class ConfirmFrame(Frame):
    def __init__(self, parent, studentId):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.studentId = studentId

    def center_window(self):
        screenWidth = self.parent.winfo_screenwidth()
        screenHeight = self.parent.winfo_screenheight()

        x = (screenWidth / 2) - (300 / 2)
        y = (screenHeight / 2) - (300 / 2)

        self.parent.geometry('%dx%d+%d+%d' % (300, 100, x, y))

    def initUI(self):
        self.center_window()
        self.parent.title("Attention")
        self.pack(fill = BOTH, expand = 1)

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)

        ConfirmFrameLabel = Label(self, text = "Are you sure you want to select these courses?", font = (16))
        ConfirmFrameLabel.grid(row = 0, column = 0, sticky = S)
        
        yesButton = Button(self, text = "Yes", command = self.confirmCourses)
        yesButton.grid(row = 1, column = 0)

        noButton = Button(self, text = "No", command = self.cancelCourses)
        noButton.grid(row = 2, column = 0)

    def confirmCourses(self):
        s.addStudentCourses(self.studentId, selected_courses)
        self.destroy()
        TimetableFrame(self.parent, self.studentId)
        

    def cancelCourses(self):
        self.parent.destroy()
        
        
def main():
    root = Tk()
    root.geometry("450x400+400+400")
    app = MainFrame(root, 2)
    root.mainloop()

if __name__ == '__main__':
    main()

        
        
