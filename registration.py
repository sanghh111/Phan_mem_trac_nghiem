from DB import *
from tkinter import *

class registration(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master=master
        self.passWord=StringVar()
        self.account=StringVar()
        self.con,self.cur=connect_DB("Sinhvien.db")
        self.display()

    def display(self):
        A=Label(self.master,text="Account")
        B=Entry(self.master,textvariable=self.account)
        C=Label(self.master,text="Passworld")
        D=Entry(self.master,textvariable=self.passWord)
        A.grid(column=0,row=0)
        B.grid(column=1,row=0)
        C.grid(column=0,row=1)
        D.grid(column=1,row=1)
        E=Button(self.master,text="OK",command=self.reg)
        F=Button(self.master,text="Cancel",command=self.master.destroy)
        E.grid(column=2,row=2)
        F.grid(column=0,row=2)
        self.mainloop()

    def reg(self):
        arrId=Select_SV(self.cur)
        success=True
        for i in arrId:
            if self.account.get() in i :      
                success=False
                return 
        if success:
            Insert_SV(self.cur,self.con,self.account.get(),self.passWord.get())
            self.master.destroy()
registration(Tk())