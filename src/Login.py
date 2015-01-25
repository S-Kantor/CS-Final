##
# Name: David Landsman, Eytan Mezhibovsky, Aaron Nahum, Sam Kantor
# File name: Login.py
# Description: Contains UI code for the LoginFrame and the CreateAccountFrame
##

from tkinter import *
from SQLWrapper import *
from Selection import *
from Timetable import *
from PreviewTimetable import *

sqlWrapper = SQLWrapper()
root = Tk()

class LoginFrame(Frame):
    def __init__(self, parent):
        '''Initializes a LoginFrame.'''
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def centerWindow(self):
        '''Centers the window on the screen.'''
        screenWidth = self.parent.winfo_screenwidth()
        screenHeight = self.parent.winfo_screenheight()

        # Calculate (x, y) position of window
        x = (screenWidth/2) - (300/2)
        y = (screenHeight/2) - (300/2)

        self.parent.geometry('%dx%d+%d+%d' % (300, 300, x, y))

    def initUI(self):
        '''Initializes the user interface by configuring the table layout (rows and columns),
        adding buttons, etc.'''
        self.parent.title("Login")
        self.centerWindow()

        # Make the window non-resizable
        self.parent.resizable(width=FALSE, height=FALSE)
        self.pack(fill=BOTH, expand=1)

        # Configure table layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)

        # Login title
        loginLabel = Label(self, text="Login", font=(16))  
        loginLabel.grid(row=0, column=0, sticky=S)

        # StudentId title
        idLabel = Label(self, text="Student ID:")
        idLabel.grid(row=1, column=0, sticky=S)
        # StudentId textbox
        self.idText = Entry(self)
        self.idText.grid(row=2, column=0)

        # Password title
        passwordLabel = Label(self, text="Password:")
        passwordLabel.grid(row=3, column=0, sticky=S)
        # Password textbox (define it to show astersiks instead of characters)
        self.passwordText = Entry(self, show="*")
        self.passwordText.grid(row=4, column=0)

        loginButton = Button(self, text="Login", command = self.login)
        loginButton.grid(row=5, column=0)

        # Create account button
        createButton = Button(self, text="Create Account", command = self.createAccount)
        createButton.grid(row=6, column=0)
        
    def login(self):
        '''Called from loginButton.
        Retrieves information from studentId and password textboxes and compares with database.
        '''
        # Retrieve student model from the database using provided studentId
        student = sqlWrapper.getStudent(self.idText.get())

        # Verify that the student exists and the password matches
        if student != None and student.password == self.passwordText.get():
            # Check if the student has already selected his final courses
            if student.finalCourses == "None" and student.selectedCourses == "None":
                # If he didn't, and he didn't select any courses, show selection screen
                self.destroy()
                SelectionFrame(self.parent, student.studentId)
            elif student.finalCourses == "None":
                # If the student already completed course selection, show him the timetable creator
                self.destroy()
                TimetableFrame(self.parent, student.studentId)
            else:
                # If he did, create a timetable preview window
                self.destroy()
                PreviewTimetableFrame(self.parent, student.studentId)
        else:
            messagebox.showerror("Error", "Incorrect credentials!")

    def createAccount(self):
        '''Called from createButton.
        Initializes a CreateAccountFrame.
        '''
        self.newWindow = Toplevel(self.master)
        CreateAccountFrame(self.newWindow)

class CreateAccountFrame(Frame):
    def __init__(self, parent):
        '''Initializes a CreateAccountFrame.'''
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def centerWindow(self):
        '''Centers the window.'''
        screenWidth = self.parent.winfo_screenwidth()
        screenHeight = self.parent.winfo_screenheight()

        # Calculate (x, y) position of window
        x = (screenWidth/2) - (300/2)
        y = (screenHeight/2) - (300/2)

        self.parent.geometry('%dx%d+%d+%d' % (300, 300, x, y))

    def initUI(self):
        '''Initializes the user interface by configuring table layout, labels, buttons.'''

        self.centerWindow()
        
        self.parent.title("Create an Account")
        
        self.pack(fill=BOTH, expand=1)

        # Configure table layout
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)

        createAccountLabel = Label(self, text="Create an Account", font=(16))
        createAccountLabel.grid(row=0, column=0, sticky=S)

        # StudentId title
        idLabel = Label(self, text="Student ID:")
        idLabel.grid(row=1, column=0, sticky=S)
        # StudentId textbox
        self.idText = Entry(self)
        self.idText.grid(row=2, column=0)

        # Password title
        passwordLabel = Label(self, text="Password:")
        passwordLabel.grid(row=3, column=0, sticky=S)
        # Password textbox
        self.passwordText = Entry(self, show="*")
        self.passwordText.grid(row=4, column=0)

        # Grade title
        gradeLabel = Label(self, text="Grade:")
        gradeLabel.grid(row=5, column=0, sticky=S)

        # Grade selection box (option menu)
        # gradeVariable stores the currently selected option
        self.gradeVariable = StringVar(self.parent)
        self.gradeVariable.set("9")
        self.gradeSelection = OptionMenu(self, self.gradeVariable, "9", "10", "11", "12")
        self.gradeSelection.grid(row=6, column=0, sticky=N)

        # Create Account button
        createAccButton = Button(self, text="Create Account", command = self.createAccount)
        createAccButton.grid(row=7, column=0)

    def createAccount(self): #checks if the given credentials can be used to make a new account, and makes one if the information isn't used
        if len(self.passwordText.get()) == 0:
            messagebox.showinfo("Info", "Please enter a password.")
        elif sqlWrapper.getStudent(self.idText.get()) != None:
            messagebox.showerror("Error", "StudentId already in use!")
        else:
            # Add the student to the database (with id, grade and password)
            sqlWrapper.addStudent(self.idText.get(), self.gradeVariable.get(), self.passwordText.get())
            self.parent.destroy()
    
def main():
    LoginFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
