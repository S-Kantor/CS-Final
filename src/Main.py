##
# Name: Sam Kantor
# Date: 11/17/2014
# Assignment: New Window
##


from tkinter import *

class MainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):
        self.parent.title("Course Selection Screen")


        idLabel = Label(self, text="Course Selection:", font=(26))
        idLabel.grid(row=0, columnspan=20, column=0, sticky=S)

        #####
        
        Box1ID = Label(self, text="Department:")
        Box1ID.grid(row=1, column=0, sticky=S)
        
        scroller1 = Scrollbar(self, orient="vertical")
        Box1 = Listbox(self, width=30, height=20, yscrollcommand=scroller1.set)
        scroller1.config(command=Box1.yview)

        Box1.grid(row=2, column=0)
        scroller1.grid(sticky=E, row = 2, rowspan = 100, column = 1, ipady = 138)

        loginButton = Button(self, text="Choose Course")
        loginButton.grid(row=3, column=0)
        
        #####

        Box2ID = Label(self, text="Course:")
        Box2ID.grid(row=1, column=2, sticky=S)
        
        scroller2 = Scrollbar(self, orient="vertical")
        Box2 = Listbox(self, width=30, height=20, yscrollcommand=scroller2.set)
        scroller2.config(command=Box2.yview)

        Box2.grid(row=2, column=2)
        scroller2.grid(sticky=E, row = 2, rowspan = 100, column = 3, ipady = 138)

        submitButton = Button(self, text="Submit Course")
        submitButton.grid(row=3, column=2)
        
        #####

        self.pack()
        
def main():
    root = Tk()
    root.geometry("450x400+400+400")
    app = MainFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()

        
        
