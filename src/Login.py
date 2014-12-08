##
# Name: Sam Kantor
#
#
##

from tkinter import *
from SQLWrapper import *
s = SQLWrapper()

class LoginFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def center_window(self):
        screenWidth = self.parent.winfo_screenwidth()
        screenHeight = self.parent.winfo_screenheight()

        # Calculate (x, y) position of window
        x = (screenWidth/2) - (300/2)
        y = (screenHeight/2) - (300/2)

        self.parent.geometry('%dx%d+%d+%d' % (300, 300, x, y))

    def initUI(self):
        self.center_window()
        self.parent.title("Login")
        self.parent.resizable(width=FALSE, height=FALSE)
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)

        loginLabel = Label(self, text="Login", font=(16))  
        loginLabel.grid(row=0, column=0, sticky=S)

        idLabel = Label(self, text="Student ID:")
        idLabel.grid(row=1, column=0, sticky=S)
        self.idText = Entry(self)
        self.idText.grid(row=2, column=0)

        passwordLabel = Label(self, text="Password:")
        passwordLabel.grid(row=3, column=0, sticky=S)
        self.passwordText = Entry(self, show="*")
        self.passwordText.grid(row=4, column=0)

        loginButton = Button(self, text="Login", command = self.login)
        loginButton.grid(row=5, column=0)

        createButton = Button(self, text="Create Account", command = self.create_account)
        createButton.grid(row=6, column=0)
        
    def login(self):
        student = s.getStudent(self.idText.get())
        if student != None and student.passwordHash == self.passwordText.get():
            print("Success")
        else:
            print("Error")
            

    def create_account(self):
        self.newWindow = Toplevel(self.master)
        self.app = CreateAccountFrame(self.newWindow)
        return

class CreateAccountFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def center_window(self):
        screenWidth = self.parent.winfo_screenwidth()
        screenHeight = self.parent.winfo_screenheight()

        # Calculate (x, y) position of window
        x = (screenWidth/2) - (300/2)
        y = (screenHeight/2) - (300/2)

        self.parent.geometry('%dx%d+%d+%d' % (300, 300, x, y))

    def initUI(self):
        self.center_window()
        self.parent.title("Create an Account")
        self.pack(fill=BOTH, expand=1)

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

        idLabel = Label(self, text="Student ID:")
        idLabel.grid(row=1, column=0, sticky=S)
        self.idText = Entry(self)
        self.idText.grid(row=2, column=0)

        passwordLabel = Label(self, text="Password:")
        passwordLabel.grid(row=3, column=0, sticky=S)
        self.passwordText = Entry(self, show="*")
        self.passwordText.grid(row=4, column=0)

        gradeLabel = Label(self, text="Grade:")
        gradeLabel.grid(row=5, column=0, sticky=S)

        self.variable = StringVar(self.parent)
        self.variable.set("9")
        self.gradeSelection = OptionMenu(self, self.variable, "9", "10", "11", "12")
        self.gradeSelection.grid(row=6, column=0, sticky=N)

        createAccButton = Button(self, text="Create Account", command = self.create_account)
        createAccButton.grid(row=7, column=0)

    def create_account(self):
        s.addStudent(self.idText.get(), self.variable.get(), self.passwordText.get())
        self.parent.destroy()
    
def main():
    root = Tk()
    app = LoginFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
