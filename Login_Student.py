from tkinter import *
class Login(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.account=StringVar()
        self.password=StringVar()
        self.display()
    
    def display(self):
        self.master.geometry("200x125")
        A=Label(self.master,text="Account")
        B=Entry(self.master,textvariable=self.account)
        C=Label(self.master,text="Passworld")
        D=Entry(self.master,textvariable=self.password)
        E=Button(self.master,text="Login")
        F=Button(self.master,text="registration")
        K=Button(self.master,text="Exit")
        A.pack()
        A.place(bordermode=OUTSIDE,x=0,y=60)
        B.pack()
        B.place(bordermode=OUTSIDE,x=60,y=60)
        C.pack()
        C.place(bordermode=OUTSIDE,x=0,y=80)
        D.pack()
        D.place(bordermode=OUTSIDE,x=60,y=80)
        E.pack()
        E.place(bordermode=OUTSIDE,x=0,y=100)
        F.pack()
        F.place(bordermode=OUTSIDE,x=70,y=100)
        K.pack()
        K.place(bordermode=OUTSIDE,x=170,y=100)
        self.master.bind('<Button-1>',self.motion)
        self.master.mainloop()
    
    def motion(self,event):
        print(event.x,event.y)
App=Login(Tk())