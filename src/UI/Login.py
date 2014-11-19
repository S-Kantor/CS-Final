##
# Name: Sam Kantor
#
#
##

import tkinter as tk

class Login ():

    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Login Screen")
        self.login_button = tk.Button(self.frame, text = "Login!", width = 25,
                                 command = self.login)
        self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25,
                                    command = self.close_windows)
        self.login_button.pack()
        self.quitButton.pack()
        self.frame.pack()
        
    def login(self):
        self.login = Test()
    def close_windows(self):
        self.master.destroy()

class Test ():

    def __init__ (self):
        print ("Login Success!")
    
    
    
def main(): 
    root = tk.Tk()
    app = Login(root)
    Login.mainloop()

if __name__ == '__main__':
    main()
