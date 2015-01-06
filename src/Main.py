##
# Name: Sam Kantor
# Date: 11/17/2014
# Assignment: New Window
##


from tkinter import *
from SQLWrapper import *
s = SQLWrapper()
selected_courses = []

class MainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.geometry("450x400+400+400")
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

        submitButton = Button(self, text="Submit Course")
        submitButton.grid(row=3, column=2)
        
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

        loginButton = Button(self, text="Choose Course", command = self.chooseCourse)
        loginButton.grid(row=3, column=0)
        
        #####

        self.pack()

    def chooseCourse(self):
        selection = self.availableCoursesBox.get(self.availableCoursesBox.curselection()[0]) # get selected string
        if len(selected_courses) < 5 and selection not in selected_courses:           
            if len(selection) > 0:
                self.selectedCoursesBox.insert(END, selection)
                selected_courses.append(selection)
            
            
        
        
def main():
    root = Tk()
    root.geometry("450x400+400+400")
    app = MainFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()

        
        
