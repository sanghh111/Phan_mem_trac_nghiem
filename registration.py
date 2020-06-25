from DB import *
from tkinter import *
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
        success=Insert_SV(self.cur,self.con,self.account.get(),passWord,salt)
        if success:
            print("True")
        else:
            print("False")
        self.master.destroy()