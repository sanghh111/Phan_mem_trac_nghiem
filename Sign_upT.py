from tkinter import *
from DB import *
import hashlib
import string
import random
def randomString(stringLength=6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
class registration(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master=master
        self.passWord=StringVar()
        self.account=StringVar()
        self.Class=StringVar()
        self.name=StringVar()
        self.birth=StringVar()
        self.sex=StringVar()
        self.phone=StringVar()
        self.email=StringVar()
        self.con,self.cur=connect_DB("Sinhvien.db")
        self.display()

    def display(self):
        A=Label(self.master,text="Id")
        B=Entry(self.master,textvariable=self.account)
        C=Label(self.master,text="Passworld")
        D=Entry(self.master,textvariable=self.passWord)
        A.grid(column=0,row=0)
        B.grid(column=1,row=0)
        C.grid(column=0,row=1)
        D.grid(column=1,row=1)
        E=Button(self.master,text="OK",command=self.reg)
        F=Button(self.master,text="Cancel",command=self.master.destroy)
        E.grid(column=2,row=8)
        F.grid(column=0,row=8)
        Label(self.master,text="Class").grid(column=0,row=2)
        Entry(self.master,textvariable=self.Class).grid(column=1,row=2)
        Label(self.master,text="Name").grid(column=0,row=3)
        Entry(self.master,textvariable=self.name).grid(column=1,row=3)
        Label(self.master,text="Birthday").grid(column=0,row=4)
        Entry(self.master,textvariable=self.birth).grid(column=1,row=4)
        Label(self.master,text="Gender").grid(column=0,row=5)
        Entry(self.master,textvariable=self.sex).grid(column=1,row=5)
        Label(self.master,text="Phone").grid(column=0,row=6)
        Entry(self.master,textvariable=self.phone).grid(column=1,row=6)
        Label(self.master,text="Email").grid(column=0,row=7)
        Entry(self.master,textvariable=self.email).grid(column=1,row=7)
        self.mainloop()

    def reg(self):
        arrId=Select_T(self.cur)
        for i in arrId:
            if self.account.get() in i :      
                return 
        salt=randomString()
        passWord=self.passWord.get()+salt
        print(passWord)
        mk= hashlib.md5(passWord.encode('utf-8')).hexdigest()
        # print(mk)
        passWord=mk
        # print(passWord)
        # mk.update(self.passWord.encode())
        a=Insert_T(self.cur,self.con,self.account.get(),passWord,salt)
        print(a)
        a=Insert_IT(self.cur,self.con,self.account.get(),self.Class.get(),self.name.get(),self.birth.get(),self.sex.get(),self.phone.get(),self.email.get())
        print(a)
        self.master.destroy()