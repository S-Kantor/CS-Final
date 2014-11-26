##
# Name: Sam Kantor
#
#
##

from tkinter import *
    

class LoginFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Login")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

        loginLabel = Label(self, text="Login", font=(16))  
        loginLabel.grid(row=0, column=0, sticky=S)

        idLabel = Label(self, text="Student ID:")
        idLabel.grid(row=1, column=0, sticky=S)
        idText = Entry(self)
        idText.grid(row=2, column=0)

        passwordLabel = Label(self, text="Password:")
        passwordLabel.grid(row=3, column=0, sticky=S)
        passwordText = Entry(self)
        passwordText.grid(row=4, column=0)

        loginButton = Button(self, text="Login", command = self.login)
        loginButton.grid(row=5, column=0)

    def login(self):
        return

class CreateAccountFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()l

    def initUI(self):
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

        createAccountLabel = Label(self, text="Create an Account", font=(16))
        createAccountLabel.grid(row=0, column=0, sticky=S)

        idLabel = Label(self, text="Student ID:")
        idLabel.grid(row=1, column=0, sticky=S)
        idText = Entry(self)
        idText.grid(row=2, column=0)

        passwordLabel = Label(self, text="Password:")
        passwordLabel.grid(row=3, column=0, sticky=S)
        passwordText = Entry(self)
        passwordText.grid(row=4, column=0)

        gradeLabel = Label(self, text="Grade:")
        gradeLabel.grid(row=5, column=0, sticky=S)

        variable = StringVar(master)
        variable.set("9")
        gradeSelection = OptionMenu(self, variable, "9", "10", "11", "12")
        gradeSelection.grid(row=6, column=0, sticky=S)
    
def main():
    root = Tk()
    root.geometry("350x300+300+300")
    app = LoginFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
