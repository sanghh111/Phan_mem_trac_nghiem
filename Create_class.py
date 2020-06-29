from tkinter import *
from DB1 import *
import string
import random
import os
def randomString(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
class create_class(Frame):
    def __init__(self,master,id):
        Frame.__init__(self,master)
        self.master=master
        self.id=id
        self.con,self.cur=connect_DB("Sinhvien.db")
        self.value=[StringVar() for i in range(0,2)]
        self.display()

    def display(self):
        Label(self.master,text="ID class").grid(row=0,column=0)
        Entry(self.master,textvariable=self.value[0]).grid(row=0,column=1)
        Label(self.master,text="Name class").grid(row=1,column=0)
        Entry(self.master,textvariable=self.value[1]).grid(row=1,column=1)
        Button(self.master,text="OK",command=self.ok).grid(row=2,column=2)
        self.master.mainloop()

    def ok(self):
        key=randomString()
        print(self.value[0].get())
        if Insert_Class(self.con,self.cur,self.value[0].get(),self.id,self.value[1].get(),key):
            path="./Class/"+self.value[0].get()+"_"+self.value[1].get()
            print(path)
            os.mkdir(path, 0o755)
        self.master.destroy()