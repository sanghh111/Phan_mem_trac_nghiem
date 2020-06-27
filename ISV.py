from tkinter import *
from DB import *

class ifs(Frame):
    def __init__(self,master,ID):
        Frame.__init__(self,master)
        self.master=master
        self.ID=ID
        self.Class=StringVar()
        self.name=StringVar()
        self.birth=StringVar()
        self.sex=StringVar()
        self.phone=StringVar()
        self.email=StringVar()
        self.con,self.cur=connect_DB("Sinhvien.db")
        self.display()

    def display(self):
        Label(self.master,text="Id").grid(column=0,row=0)
        Label(self.master,text=self.ID).grid(column=1,row=0)
        Label(self.master,text="Class").grid(column=0,row=1)
        Entry(self.master,textvariable=self.Class).grid(column=1,row=1)
        Label(self.master,text="Name").grid(column=0,row=2)
        Entry(self.master,textvariable=self.name).grid(column=1,row=2)
        Label(self.master,text="Birthday").grid(column=0,row=3)
        Entry(self.master,textvariable=self.birth).grid(column=1,row=3)
        Label(self.master,text="Sex").grid(column=0,row=4)
        Entry(self.master,textvariable=self.sex).grid(column=1,row=4)
        Label(self.master,text="Phone").grid(column=0,row=5)
        Entry(self.master,textvariable=self.phone).grid(column=1,row=5)
        Label(self.master,text="Email").grid(column=0,row=6)
        Entry(self.master,textvariable=self.email).grid(column=1,row=6)
        Button(self.master,text="OK",command=self.Ok).grid(column=3,row=7)

        self.master.mainloop()

    def Ok(self):
        a=Insert_ISV(self.cur,self.con,self.ID,self.Class,self.name,self.birth,self.sex,self.phone,self.email)
        print(a)
        if a:
            return True
        pass
