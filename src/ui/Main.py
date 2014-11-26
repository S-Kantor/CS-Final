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
        self.parent.title("Main Screen")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.grid()

        self.available = Listbox(self)
        self.available.grid(row=0, column=0, rowspan=2)

        self.selected = Listbox(self)
        self.selected.grid(row=0, column=1, rowspan=2)

        for i in range(100):
            self.available.insert(END, str(i))
        
def main():
    root = Tk()
    root.geometry("450x400+400+400")
    app = MainFrame(root)
    root.mainloop()

if __name__ == '__main__':
    main()

        
        
