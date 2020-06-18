from tkinter import *

class Join_class(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.display()
    
    def display(self):
        self.master.geometry("200x125")

        self.master.mainloop()
    