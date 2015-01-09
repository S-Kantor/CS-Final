
#########################################
# Programmer: Eytan Mezhibovsky
# Group: Aaron, David, Eytan, Shmuel
# Date: December 9th, 2014
# File Name: Course selection screen
# Description:  GUI for course selection for timetable final project
#########################################

from tkinter import *
from SQLWrapper import *
s = SQLWrapper()

class MainFrame(Frame):
    def __init__(self, parent, studentId):
        Frame.__init__(self, parent)

        self.parent = parent

        self.studentId = 2

        self.initUI()

    def initUI(self):
        self.parent.title("Semester Organizer")
        self.parent.resizable(width=FALSE, height=FALSE)
        self.pack(fill=BOTH, expand=1)

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
        
        idLabel = Label(self, text="Course Selection:", font=(26))
        idLabel.grid(row=0, columnspan=20, column=0, sticky=S)

        #####
        
        Box1ID = Label(self, text="Semester 1:")
        Box1ID.grid(row=1, column=0, sticky=S)

        Button_1Left = Button(self,text="")
        Button_1Left.grid(row=2, column=0)

        Button_2Left = Button(self,text="")
        Button_2Left.grid(row=3, column=0)

        Button_3Left = Button(self,text="")
        Button_3Left.grid(row=4, column=0)

        Button_4Left = Button(self,text="")
        Button_4Left.grid(row=5, column=0)

        Button_5Left = Button(self,text="")
        Button_5Left.grid(row=6, column=0)
        
        
        #####

        Box2ID = Label(self, text="Semester 2:")
        Box2ID.grid(row=1, column=1, sticky=S)

        Button_1Right = Button(self,text="")
        Button_1Right.grid(row=2, column=1)

        Button_2Right = Button(self,text="")
        Button_2Right.grid(row=3, column=1)

        Button_3Right = Button(self,text="")
        Button_3Right.grid(row=4, column=1)

        Button_4Right = Button(self,text="")
        Button_4Right.grid(row=5, column=1)

        Button_5Right = Button(self,text="")
        Button_5Right.grid(row=6, column=1)

        submitButton = Button(self, text="Submit")
        submitButton.grid(row=7, column=0, columnspan=2)
        
        #####
        Box1ID = Label(self, text="Course List:")
        Box1ID.grid(row=1, column=2, sticky=S)
        
        scroller1 = Scrollbar(self, orient="vertical")
        self.Box1 = Listbox(self, width=30, height=20, yscrollcommand=scroller1.set)
        scroller1.config(command=self.Box1.yview)

        self.Box1.grid(row=2, column=2, rowspan=5)
        scroller1.grid(sticky=E, row = 2, rowspan=5, column = 1, ipady = 138)

        loginButton = Button(self, text="Choose Course")
        loginButton.grid(row=7, column=2)

        for course in s.getStudent(self.studentId):
            self.Box1.insert(END, course.name)

        
def main():
    root = Tk()
    root.geometry("600x450+300+300")
    app = MainFrame(root, 2)
    root.mainloop()

if __name__ == '__main__':
    main()
