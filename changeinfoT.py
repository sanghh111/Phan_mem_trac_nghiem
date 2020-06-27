from tkinter import *
from DB import *
class Change(Frame):
    def __init__(self,master,id):
        Frame.__init__(self,master)
        self.master=master
        self.id=id
        self.Boo=[BooleanVar() for i in range(0,7)]
        self.Check=[ None for i in range(0,8)]
        self.Label=[None for i in range(0,8)]
        self.Entry=[None for i in range(0,8)]
        self.count=0
        self.value=[StringVar() for i in range(0,8)]
        self.con,self.cur=connect_DB("Sinhvien.db")
        self.arr_info=Select_IT(self.cur,self.id)
        print(self.arr_info)
        for i in self.arr_info[1:]:
            self.value[self.count].set(i)
            self.count+=1
        self.display()
    
    def display(self):
        Label(self.master,text="id").grid(column=0,row=0)
        Label(self.master,text=self.id).grid(column=1,row=0)
        #IDMA
        self.Label[0]=Label(self.master,text="ID MAJOR")
        self.Label[0].grid(column=0,row=1)
        self.Check[0]=Checkbutton(self.master,variable=self.Boo[0],command=self.IDMA)
        self.Check[0].grid(column=1,row=1)

        #Name
        self.Label[1]=Label(self.master,text="Name")
        self.Label[1].grid(column=0,row=2)
        self.Check[1]=Checkbutton(self.master,variable=self.Boo[1],command=self.name)
        self.Check[1].grid(column=1,row=2)

        #Birthday
        self.Label[2]=Label(self.master,text="BirthDay")
        self.Label[2].grid(column=0,row=3)
        self.Check[2]=Checkbutton(self.master,variable=self.Boo[2],command=self.birth)
        self.Check[2].grid(column=1,row=3)

        #Gender
        self.Label[3]=Label(self.master,text="Gender")
        self.Label[3].grid(column=0,row=4)
        self.Check[3]=Checkbutton(self.master,variable=self.Boo[3],command=self.Gender)
        self.Check[3].grid(column=1,row=4)

        #Phone
        self.Label[4]=Label(self.master,text="Phone")
        self.Label[4].grid(column=0,row=5)
        self.Check[4]=Checkbutton(self.master,variable=self.Boo[4],command=self.phone)
        self.Check[4].grid(column=1,row=5)
        
        #Email
        self.Label[5]=Label(self.master,text="email")
        self.Label[5].grid(column=0,row=6)
        self.Check[5]=Checkbutton(self.master,variable=self.Boo[5],command=self.email)
        self.Check[5].grid(column=1,row=6)

        #pass
        self.Label[6]=Label(self.master,text="pass")
        self.Label[6].grid(column=0,row=7)
        self.Check[6]=Checkbutton(self.master,variable=self.Boo[6],command=self.Pass)
        self.Check[6].grid(column=1,row=7)

        #Button
        Button(self.master,text="OK",command=self.ok).grid(column=2,row=9)
        self.master.mainloop()
        
    def IDMA(self):
        if self.Boo[0].get():
            if not self.Entry[0]:
                self.Entry[0]=Entry(self.master,textvariable=self.value[0])
                self.Entry[0].grid(column=2,row=1)
            else:
                self.Entry[0].grid(column=2,row=1)
        else :
            self.Entry[0].grid_forget()

    def name(self):
        if self.Boo[1].get():
            if not self.Entry[1]:
                self.Entry[1]=Entry(self.master,textvariable=self.value[1])
                self.Entry[1].grid(column=2,row=2)
            else:
                self.Entry[1].grid(column=2,row=2)
        else :
            self.Entry[1].grid_forget()

    def birth(self):
        if self.Boo[2].get():
            if not self.Entry[2]:
                self.Entry[2]=Entry(self.master,textvariable=self.value[2])
                self.Entry[2].grid(column=2,row=3)
            else:
                self.Entry[2].grid(column=2,row=3)
        else :
            self.Entry[2].grid_forget()

    def Gender(self):
        if self.Boo[3].get():
            if not self.Entry[3]:
                self.Entry[3]=Entry(self.master,textvariable=self.value[3])
                self.Entry[3].grid(column=2,row=4)
            else:
                self.Entry[3].grid(column=2,row=4)
        else :
            self.Entry[3].grid_forget()

    def phone(self):
        if self.Boo[4].get():
            if not self.Entry[4]:
                self.Entry[4]=Entry(self.master,textvariable=self.value[4])
                self.Entry[4].grid(column=2,row=5)
            else:
                self.Entry[4].grid(column=2,row=5)
        else :
            self.Entry[4].grid_forget()

    def email(self):
        if self.Boo[5].get():
            if not self.Entry[5]:
                self.Entry[5]=Entry(self.master,textvariable=self.value[5])
                self.Entry[5].grid(column=2,row=6)
            else:
                self.Entry[5].grid(column=2,row=6)
        else :
            self.Entry[5].grid_forget()

    def Pass(self):
        if self.Boo[6].get():
            if not self.Entry[6]:
                self.Entry[6]=Entry(self.master,textvariable=self.value[6],show="*")
                self.Entry[7]=Entry(self.master,textvariable=self.value[7],show="*")
                self.Label[7]=Label(self.master,text="Confirm Password")
                self.Label[7].grid(column=0,row=8)
                self.Entry[6].grid(column=2,row=7)
                self.Entry[7].grid(column=2,row=8)
            else:
                self.Label[7].grid(column=0,row=8)
                self.Entry[6].grid(column=2,row=7)
                self.Entry[7].grid(column=2,row=8)
        else :
            self.Entry[6].grid_forget()
            self.Entry[7].grid_forget()
            self.Label[7].grid_forget()

    def ok(self):
        count=0
        a=[]
        for i in self.Boo:
            if i.get():
                a.append(self.value[count].get())
            else :
                a.append("")
            count+=1
        # for i in a :
        #     print(i)
        a=Update_IT(self.cur,self.con,self.id,a[0],a[1],a[2],a[3],a[4],a[5])
        print(a)
        self.master.destroy()
# Change(Tk(),"123")