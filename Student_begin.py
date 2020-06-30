from Changeinfo import *
from DB1 import *
from Quick_Sort import *
from SignupClass import *
from PIL import Image, ImageTk
class Open_S(Frame):
    def __init__(self,master,id):
        Frame.__init__(self,master)
        self.master=master
        self.can=[]
        self.id=id
        self.con,self.cur=connect_DB("Sinhvien.db")
        self.arr_info=Select_ISV(self.cur,self.id)
        self.Value=StringVar()
        self.arr_class=Select_Student_Class(self.cur,self.id)
        print(self.arr_class)
        self.label=[]
        self.radi=[]
        self.load=[]
        self.hinh=[]
        self.sreach=[]
        self.sreachL=[]
        self.sreachR=[]
        self.display()

    def display(self):
        self.master.geometry("600x400")
        self.load.append(Image.open("Image\\serch25x25.png"))
        self.hinh.append(ImageTk.PhotoImage(self.load[0]))
        self.can.append(Canvas(self.master,height=250,width=200,bg="white"))
        self.can[0].pack()
        self.can[0].place(bordermode=OUTSIDE,x=0,y=0)
        self.frame=Frame(self.master,height=250,width=250)
        self.frame.pack(expand=True,fill=BOTH)
        self.frame.place(x=200,y=0)
        self.can.append(Canvas(self.frame,height=250,width=250,bg="gray",scrollregion=(0,0,500,500)))
        self.can[1].pack(expand=True,fill=BOTH)
        
        #LABEL INFO
        a=Label(self.can[0],text="THONG TIN Sinh Vien")
        a.place(x=35,y=5)
        #ID
        self.ID1=Label(self.can[0],text="ID")
        self.ID1.place(x=0,y=35)
        self.ID2=Label(self.can[0],text=self.arr_info[0])
        self.ID2.place(x=50,y=35)
        #Name
        self.Name1=Label(self.can[0],text="Name")
        self.Name1.place(x=0,y=65)
        self.Name2=Label(self.can[0],text=self.arr_info[1])
        self.Name2.place(x=50,y=65)
        #Birthday
        self.birth1=Label(self.can[0],text="Birthday")
        self.birth1.place(x=0,y=95)
        self.birth2=Label(self.can[0],text=self.arr_info[2])
        self.birth2.place(x=50,y=95)
        #Gender
        self.Gender1=Label(self.can[0],text="Gender")
        self.Gender1.place(x=0,y=125)
        self.Gender2=Label(self.can[0],text=self.arr_info[3])
        self.Gender2.place(x=50,y=125)
        #Phone
        self.Phone1=Label(self.can[0],text="Phone")
        self.Phone1.place(x=0,y=155)
        self.Phone2=Label(self.can[0],text=self.arr_info[4])
        self.Phone2.place(x=50,y=155)
        #Email
        self.Email1=Label(self.can[0],text="Email")
        self.Email1.place(x=0,y=185)
        self.Email2=Label(self.can[0],text=self.arr_info[5])
        self.Email2.place(x=50,y=185)

        Button(self.can[1],text = "My Class",command=self.list_my_class).place(x=2,y=0)
        Button(self.can[1],text = "Sign-up Class",command=self.list_sign_up).place(x=170,y=0)
        Button(self.can[1],text="ID",command=self.sort_id).place(x=10,y=25)
        Button(self.can[1],text="Name Class",command=self.sort_name).place(x=90,y=25)
        Label(self.can[1],text="State").place(x=210,y=25)
        Button(self.can[1],image=self.hinh[0],command=self.src).place(x=0,y=225)
        self.update_class()

        self.J=Button(self.master,text = "Join class",width=17,height=5,bg="yellow")
        self.J.place(x=470,y=0)
        
        self.S=Button(self.master,text = "Sign-up class",width=17,height=5,bg="blue",state=DISABLED,command=self.sign_up)
        self.S.place(x=470,y=80)
        
        C=Button(self.master,text = "Change info",bg="red",command=self.change)
        C.place(x=60,y=250)
        
        D=Button(self.master,text = "backPage",bg="orange")
        D.pack()
        D.place(x=200,y=270)
        
        E=Button(self.master,text = "nextPge",bg="orange")
        E.pack()
        E.place(x=400,y=270)
        
        self.master.mainloop()

    def change(self):
        print(self.id)
        Change(Toplevel(),self.id)
    
    def update_class(self):
        tx=10
        ty=50
        if self.sreach:
            for i in range(0,len(self.sreach)):
                self.sreachL[i][0].destroy()
                self.sreachL[i][1].destroy()
                self.radi[i].destroy()
            self.sreachL.clear()
            self.sreachR.clear()
            self.sreach.clear()
        if self.label:
            for i in range(0,len(self.label)):
                self.label[i][0].destroy()
                self.label[i][1].destroy()
                self.radi[i].destroy()
            self.label.clear()
            self.radi.clear()
        for i in range(0,len(self.arr_class)):
            try:
                self.label[i][0]
            except:
                self.label.append([None,None])
                self.radi.append(None)
        for i in range(0,len(self.arr_class)):
            self.label[i][0]=Label(self.can[1],text=self.arr_class[i][0])
            self.label[i][1]=Label(self.can[1],text=self.arr_class[i][1])
            self.radi[i]=Radiobutton(self.can[1],variable=self.Value,value=self.arr_class[i][0])
            self.radi[i].invoke()
            self.label[i][0].place(x=tx,y=ty)
            self.label[i][1].place(x=tx+80,y=ty)
            self.radi[i].place(x=tx+200,y=ty)
            ty+=20
        pass
    
    def update_data(self):
        if self.sreach:
            for i in range(0,len(self.sreach)):
                self.sreachL[i][0].destroy()
                self.sreachL[i][1].destroy()
                self.sreachR[i].destroy()
            self.sreachL.clear()
            self.sreachR.clear()
            self.sreach.clear()
        else:
            for i in range(0,len(self.label)):
                self.label[i][0].place_forget()
                self.label[i][1].place_forget()
                self.radi[i].place_forget()
        tx=10
        ty=50
        for i in range(0,len(self.label)):
            self.label[i][0].place(x=tx,y=ty)
            self.label[i][1].place(x=tx+80,y=ty)
            self.radi[i].place(x=tx+200,y=ty)
            ty+=20

    def create_class(self):
        pass

    def list_sign_up(self):
        self.S.config(state=NORMAL)
        self.J.config(state=DISABLED)
        self.arr_class.clear()
        self.arr_class=Select_Signup_Class(self.cur,self.id)
        # print(self.arr_class)
        self.update_class()
        pass

    def list_my_class(self):
        self.J.config(state=NORMAL)
        self.S.config(state=DISABLED )
        self.arr_class.clear()
        self.arr_class=Select_Student_Class(self.cur,self.id)
        self.update_class()
        pass

    def sort_id(self):
        quickSort(self.arr_class,self.label,self.radi,0,len(self.arr_class)-1)
        self.update_data()
        pass

    def sort_name(self):
        quickSort(self.arr_class,self.label,self.radi,0,len(self.arr_class)-1,1)
        self.update_data()
        pass

    def src(self):
        self.valueSrc=StringVar()
        self.valueSrc.set("ID")
        self.t1=Entry(self.can[1],textvariable=self.valueSrc)
        self.t2=Button(self.can[1],text="Ok",command=self.ok_t1)
        self.t1.place(x=30,y=235)
        self.t2.place(x=155,y=235)

    def ok_t1(self):
        if  self.sreach:
            for i in range(0,len(self.sreach)):
                self.sreachL[i][0].destroy()
                self.sreachL[i][1].destroy()
                self.sreachR[i].destroy()
        else:
            for i in range(0,len(self.arr_class)):
                self.label[i][1].place_forget()
                self.label[i][0].place_forget()
                self.radi[i].place_forget()
        self.sreach.clear()
        self.sreach=binarySearch(self.arr_class,0,len(self.arr_class)-1,self.valueSrc.get())
        tx=10
        ty=50
        for i in range(0,len(self.sreach)):
            try:
                self.sreachL[i][0]
            except:
                self.sreachL.append([None,None])
                self.sreachR.append(None)
            self.sreachL[i][0]=Label(self.can[1],text=self.sreach[i][0])
            self.sreachL[i][1]=Label(self.can[1],text=self.sreach[i][1])
            self.sreachR[i]=Radiobutton(self.can[1],variable=self.Value,value=self.sreach[i][0])
            self.sreachR[i].invoke()
            self.sreachL[i][1].place(x=tx+80,y=ty)
            self.sreachL[i][0].place(x=tx,y=ty)
            self.sreachR[i].place(x=tx+200,y=ty)
            ty+=20

    def sign_up(self):
        sign_up_class(Toplevel(),self.Value.get(),self.id)
Open_S(Tk(),"sang")