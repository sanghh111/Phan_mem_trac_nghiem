from tkinter import *
from DB import *
from registration import *
from PIL import Image, ImageTk
import hashlib
import time 
class Login(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.account=StringVar()
        self.password=StringVar()
        self.con,self.cur=connect_DB("Sinhvien.db")
        self.load=[]
        self.hinh=[]
        self.display()
    
    def display(self):
        self.load.append(Image.open("Image\\Sign-in50x50.png"))
        self.hinh.append(ImageTk.PhotoImage(self.load[0]))
        self.load.append(Image.open("Image\\GenyTeam50x50.png"))
        self.hinh.append(ImageTk.PhotoImage(self.load[1]))
        self.load.append(Image.open("Image\\Entry.png"))
        self.hinh.append(ImageTk.PhotoImage(self.load[2]))
        Label(self.master,image=self.hinh[1]).place(x=0,y=0)
        self.master.maxsize(800,500)
        A=Label(self.master,text="Account")
        B=Entry(self.master,textvariable=self.account,bg="gray",selectbackground="black")
        C=Label(self.master,text="Passworld")
        D=Entry(self.master,textvariable=self.password,show="*",bg="gray")
        E=Button(self.master,image=self.hinh[0],command=self.login)
        F=Button(self.master,text="registration",command=self.reg)
        K=Button(self.master,text="Exit")
        A.place(bordermode=OUTSIDE,x=0,y=60)
        B.place(bordermode=OUTSIDE,x=60,y=60)
        C.place(bordermode=OUTSIDE,x=0,y=80)
        D.place(bordermode=OUTSIDE,x=60,y=80)
        E.place(bordermode=OUTSIDE,x=0,y=100)
        F.place(bordermode=OUTSIDE,x=70,y=100)
        K.place(bordermode=OUTSIDE,x=170,y=100) 
        # self.master.bind('<Button-1>',self.motion)
        self.master.mainloop()

    def login(self):
        if Checkpassworld(self.cur,self.account.get(),self.password.get()):
            print("True")
        else :
            print("Flase")

    def reg(self):
        App=Toplevel()
        registration(App)

App=Login(Tk())