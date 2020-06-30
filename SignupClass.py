from tkinter import *
from DB1 import *


class sign_up_class(Frame):
    def __init__(self,master,idc,id):
        Frame.__init__(self,master)
        self.master=master
        self.idc=idc
        self.id=id
        self.con,self.cur=connect_DB("Sinhvien.db")
        self.value=StringVar()
        self.display()
    
    def display(self):
        self.master.geometry("200x125")
        Label(self.master,text="Key").grid(column=0,row=0)
        Entry(self.master,textvariable=self.value).grid(column=1,row=0)
        Button(self.master,text="OK",command=self.OK).grid(column=2,row=1)
        self.master.mainloop()

    def OK(self):
        a=Insert_DSCLASS(self.cur,self.con,self.idc,self.id,self.value.get())
        print(a)
        self.master.destroy()
