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
        
        Box2ID = Label(self, text="Course:")
        Box2ID.grid(row=1, column=2, sticky=S)
        
        scroller2 = Scrollbar(self, orient="vertical")
        self.Box2 = Listbox(self, width=30, height=20, yscrollcommand=scroller2.set)
        scroller2.config(command=self.Box2.yview)

        self.Box2.grid(row=2, column=2)
        scroller2.grid(sticky=E, row = 2, rowspan = 100, column = 3, ipady = 138)

        submitButton = Button(self, text="Submit Course")
        submitButton.grid(row=3, column=2)
        
        #####
        
        Box1ID = Label(self, text="Available Courses:")
        Box1ID.grid(row=1, column=0, sticky=S)
        
        scroller1 = Scrollbar(self, orient="vertical")
        self.Box1 = Listbox(self, width=30, height=20, yscrollcommand=scroller1.set)
        scroller1.config(command=self.Box1.yview)
        for course in s.getAllCourses():
            self.Box1.insert(END, course.name)

        self.Box1.grid(row=2, column=0)
        scroller1.grid(sticky=E, row = 2, rowspan = 100, column = 1, ipady = 138)

        loginButton = Button(self, text="Choose Course", command = self.chooseCourse)
        loginButton.grid(row=3, column=0)
        
        #####

        self.pack()

    def chooseCourse(self):
        print("Button pressed")
        selection = self.Box1.curselection()
        print(selection)
        if len(selected_courses) < 5 and selection[0] == selected_courses[i]:           
            if len(selection) > 0:
                self.Box2.insert(END, self.Box1.get(selection[0]))
                selected_courses.append(self.Box1.get(selection[0]))
            
            
        
        
def main():
    root = Tk()
    root.geometry("450x400+400+400")
    app = MainFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()

        
        
