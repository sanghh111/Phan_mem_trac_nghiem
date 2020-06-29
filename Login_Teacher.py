from Sign_upT import *
from Lecture_begin import *
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
        self.load.append(Image.open("Image\\Sign-Up100x50.png"))
        self.hinh.append(ImageTk.PhotoImage(self.load[3]))
        Label(self.master,image=self.hinh[1]).place(x=0,y=0)
        self.master.minsize(800,500)
        self.master.maxsize(800,500)
        A=Label(self.master,text="Acscount")
        B=Entry(self.master,textvariable=self.account,bg="gray",selectbackground="black")
        C=Label(self.master,text="Passworld")
        D=Entry(self.master,textvariable=self.password,show="*",bg="gray")
        E=Button(self.master,image=self.hinh[0],command=self.login)
        F=Button(self.master,image=self.hinh[3],command=self.reg)
        K=Button(self.master,text="Exit")
        A.place(bordermode=OUTSIDE,x=300,y=150)
        B.place(bordermode=OUTSIDE,x=362,y=152)
        C.place(bordermode=OUTSIDE,x=300,y=170)
        D.place(bordermode=OUTSIDE,x=362,y=172)
        E.place(bordermode=OUTSIDE,x=300,y=300)
        F.place(bordermode=OUTSIDE,x=500,y=300)
        # K.place(bordermode=OUTSIDE,x=170,y=100) 
        # self.master.bind('<Button-1>',self.motion)
        self.master.mainloop()

    def login(self):
        if Checkpassworld_T(self.cur,self.account.get(),self.password.get()):
            self.master.destroy()
            Open_S(Tk(),self.account.get())
        else :
            print("Flase")

    def reg(self):
        App=Toplevel()
        registration(App)

App=Login(Tk())