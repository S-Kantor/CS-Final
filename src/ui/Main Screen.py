##
# Name: Sam Kantor
# Date: 11/17/2014
# Assignment: New Window
##


from tkinter import *

class Main_Screen(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.columnconfig()

        self.initUI()

    def columnconfig(self):

        #Config Column 1 and rows for column one

        self.columnconfigure(0, weight=3)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)

        #Config Column 2 and rows for column two

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1) 

        

    def  initUI(self):
        self.parent.title("Main Screen")
        self.pack(fill=BOTH, expand=1)

        scrollbar = Scrollbar(self, orient=VERTICAL)
        listbox = Listbox(self, yscrollcommand=scrollbar.set)
        scrollbar.config(command=listbox.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        listbox.pack(side=LEFT, fill=BOTH, expand=1)

    def addCourse(self):
        print ("Do nothing")



def main():
    root = Tk()
    RTitle=root.title("Main Screen")
    root.geometry("450x400+400+400")
    app = Main_Screen(root)
    root.mainloop()

if __name__ == '__main__':
    main()

        
        
