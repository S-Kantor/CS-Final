
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
selected_courses = []

class TimetableFrame(Frame):
    def __init__(self, parent, studentId):
        Frame.__init__(self, parent)

        self.parent = parent

        self.studentId = studentId

        self.initUI()

    def initUI(self):
        self.parent.title("Semester Organizer")
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
        #for column in range(0,1):
            #for row in range(2, 6):
        
        Box1ID = Label(self, text="Semester 1:")
        Box1ID.grid(row=1, column=0, sticky=S)

        self.Button_1Left = Button(self,text="", command = self.selectPeriod1)
        self.Button_1Left.grid(row=2, column=0)

        self.Button_2Left = Button(self,text="", command = self.selectPeriod2)
        self.Button_2Left.grid(row=3, column=0)

        self.Button_3Left = Button(self,text="", command = self.selectPeriod3)
        self.Button_3Left.grid(row=4, column=0)

        self.Button_4Left = Button(self,text="", command = self.selectPeriod4)
        self.Button_4Left.grid(row=5, column=0)

        self.Button_5Left = Button(self,text="", command = self.selectPeriod5)
        self.Button_5Left.grid(row=6, column=0)

        #self.semester1 = [self.Button_1Left, self.Button_2Left, self.Button_3Left, self.Button_4Left, self.Button_5Left]
        
        
        #####

        Box2ID = Label(self, text="Semester 2:")
        Box2ID.grid(row=1, column=1, sticky=S)

        self.Button_1Right = Button(self,text="", command = self.selectPeriod6)
        self.Button_1Right.grid(row=2, column=1)

        self.Button_2Right = Button(self,text="", command = self.selectPeriod7)
        self.Button_2Right.grid(row=3, column=1)

        self.Button_3Right = Button(self,text="", command = self.selectPeriod8)
        self.Button_3Right.grid(row=4, column=1)

        self.Button_4Right = Button(self,text="", command = self.selectPeriod9)
        self.Button_4Right.grid(row=5, column=1)

        self.Button_5Right = Button(self,text="", command = self.selectPeriod10)
        self.Button_5Right.grid(row=6, column=1)

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

        self.selected_courses = eval(s.getStudent(self.studentId).selectedCourses)

        for course in self.selected_courses:
            self.Box1.insert(END, course)
            

    #def selectCourse1(self):
        #selection = self.Box1.get(self.Box1.curselection()[0])
        #for i in self.semester1:
            #self.semester1[i-1]["text"] = selection
        #self.pack()

    def removeFromListbox(self, selection):
        self.selected_courses.remove(selection)
        self.Box1.delete(ANCHOR)

    #def removeFromButton(self, selection):
        #self.Box1.insert(selection)
        #self.Button["text"] = ""

    def selectPeriod1(self):
        if self.Button_1Left["text"] != "":
            selection = self.Button_1Left["text"]
            self.Box1.insert(END, selection)
            self.Button_1Left["text"] = ""
            self.selected_courses.append(selection)
        else:
            selection = self.Box1.get(self.Box1.curselection()[0])
            self.Button_1Left["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod2(self):
        if self.Button_2Left["text"] != "":
            selection = self.Button_2Left["text"]
            self.Box1.insert(END, selection)
            self.Button_2Left["text"] = ""
            self.selected_courses.append(selection)
        else:
            selection = self.Box1.get(self.Box1.curselection()[0])
            self.Button_2Left["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod3(self):
        if self.Button_3Left["text"] != "":
            selection = self.Button_3Left["text"]
            self.Box1.insert(END, selection)
            self.Button_3Left["text"] = ""
            self.selected_courses.append(selection)
        else:
            selection = self.Box1.get(self.Box1.curselection()[0])
            self.Button_3Left["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod4(self):
        if self.Button_4Left["text"] != "":
            selection = self.Button_4Left["text"]
            self.Box1.insert(END, selection)
            self.Button_4Left["text"] = ""
            self.selected_courses.append(selection)
        else:
            selection = self.Box1.get(self.Box1.curselection()[0])
            self.Button_4Left["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod5(self):
        if self.Button_5Left["text"] != "":
            selection = self.Button_5Left["text"]
            self.Box1.insert(END, selection)
            self.Button_5Left["text"] = ""
            self.selected_courses.append(selection)
        else:
            selection = self.Box1.get(self.Box1.curselection()[0])
            self.Button_5Left["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod6(self):
        if self.Button_1Right["text"] != "":
            selection = self.Button_1Right["text"]
            self.Box1.insert(END, selection)
            self.Button_1Right["text"] = ""
            self.selected_courses.append(selection)
        else:
            selection = self.Box1.get(self.Box1.curselection()[0])
            self.Button_1Right["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod7(self):
        if self.Button_2Right["text"] != "":
            selection = self.Button_2Right["text"]
            self.Box1.insert(END, selection)
            self.Button_2Right["text"] = ""
            self.selected_courses.append(selection)
        else:
            selection = self.Box1.get(self.Box1.curselection()[0])
            self.Button_2Right["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod8(self):
        if self.Button_3Right["text"] != "":
            selection = self.Button_3Right["text"]
            self.Box1.insert(END, selection)
            self.Button_3Right["text"] = ""
            self.selected_courses.append(selection)
        else:
            selection = self.Box3.get(self.Box1.curselection()[0])
            self.Button_1Right["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod9(self):
        if self.Button_4Right["text"] != "":
            selection = self.Button_4Right["text"]
            self.Box1.insert(END, selection)
            self.Button_4Right["text"] = ""
            self.selected_courses.append(selection)
        else:
            selection = self.Box1.get(self.Box1.curselection()[0])
            self.Button_4Right["text"] = selection
            self.removeFromListbox(selection)

    def selectPeriod10(self):
        if self.Button_5Right["text"] != "":
            selection = self.Button_5Right["text"]
            self.Box1.insert(END, selection)
            self.Button_5Right["text"] = ""
            self.selected_courses.append(selection)
        else:
            selection = self.Box1.get(self.Box1.curselection()[0])
            self.Button_5Right["text"] = selection
            self.removeFromListbox(selection)

        
def main():
    root = Tk()
    root.geometry("600x450+300+300")
    app = TimetableFrame(root, 2)
    root.mainloop()

if __name__ == '__main__':
    main()
