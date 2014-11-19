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

        self.columconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        loginLabel = Label(self, text="Login")
        loginLabel.grid(row=0, column=0)

        idText = Text(self)
        idText.grid(row=1, column=0)

        passwordText = Text(self)
        passwordText.grid(row=2, column=0)

        loginButton = Button(self, text="Login")
        loginButton.grid(row=3, column=0)
    
def main():
    root = Tk()
    root.geometry("350x300+300+300")
    app = LoginFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()
