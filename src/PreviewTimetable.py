
#########################################
# Programmer: Eytan Mezhibovsky
# Group: Aaron, David, Eytan, Shmuel
# Date: December 9th, 2014
# File Name: Course selection screen
# Description:  GUI for course selection for timetable final project
#########################################

from tkinter import *
from SQLWrapper import *
from Timetable import *
s = SQLWrapper()

class FinalTimetableFrame(Frame):
    def __init__(self, parent, studentId):
        Frame.__init__(self, parent)

        self.parent = parent

        self.studentId = studentId

        self.student = s.getStudent(self.studentId)
        self.finalCourses = eval(self.student.finalCourses)

        self.initUI()

    def initUI(self):
        self.parent.geometry("650x450+300+300") #window size
        self.parent.title("Semester Organizer")
        self.pack(fill=BOTH, expand=1)

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
        
        idLabel = Label(self, text="Final Courses:", font=(26))
        idLabel.grid(row=0, columnspan=20, column=0, sticky=S)

        #####
        
        Box1ID = Label(self, text="Semester 1:")
        Box1ID.grid(row=1, column=0, sticky=S)

        #Non-functioning buttons for each period slot on the timetable
        self.Button_1Left = Button(self,text=self.finalCourses[0])
        self.Button_1Left.grid(row=2, column=0)

        self.Button_2Left = Button(self,text=self.finalCourses[1])
        self.Button_2Left.grid(row=3, column=0)

        self.Button_3Left = Button(self,text=self.finalCourses[2])
        self.Button_3Left.grid(row=4, column=0)

        self.Button_4Left = Button(self,text=self.finalCourses[3])
        self.Button_4Left.grid(row=5, column=0)

        self.Button_5Left = Button(self,text=self.finalCourses[4])
        self.Button_5Left.grid(row=6, column=0)
        
        #####

        Box2ID = Label(self, text="Semester 2:")
        Box2ID.grid(row=1, column=1, sticky=S)

        self.Button_1Right = Button(self,text=self.finalCourses[5])
        self.Button_1Right.grid(row=2, column=1)

        self.Button_2Right = Button(self,text=self.finalCourses[6])
        self.Button_2Right.grid(row=3, column=1)

        self.Button_3Right = Button(self,text=self.finalCourses[7])
        self.Button_3Right.grid(row=4, column=1)

        self.Button_4Right = Button(self,text=self.finalCourses[8])
        self.Button_4Right.grid(row=5, column=1)

        self.Button_5Right = Button(self,text=self.finalCourses[9])
        self.Button_5Right.grid(row=6, column=1)
        
        #####

        self.selected_courses = eval(s.getStudent(self.studentId).selectedCourses)

        
def main():
    root = Tk()
    #root.geometry("600x450+300+300")
    app = TimetableFrame(root, 2)
    root.mainloop()

if __name__ == '__main__':
    main()
