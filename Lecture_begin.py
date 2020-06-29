from Create_class import create_class
from Quick_Sort import*
from changeinfoT import*
from PIL import Image, ImageTk
from DB1 import *
class Open_S(Frame):
    def __init__(self,master,id):
        Frame.__init__(self,master)
        self.master=master
        self.can=[]
        self.id=id
        self.con,self.cur=connect_DB("Sinhvien.db")
        self.arr_info=Select_IT(self.cur,self.id)
        self.arr_class=Select_ClasS_IDT(self.cur,self.id)
        a=len(self.arr_class)
        self.boo=StringVar()
        self.Label=[[[] for i in range(0,2) ] for i in range (0,a)]
        self.radi=[None for i in range(0,a)]
        self.load=[]
        self.hinh=[]
        self.pos=0
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
        self.can.append(Canvas(self.frame,height=250,width=250,bg="gray",))
        self.can[1].pack()
        
        #LABEL INFO
        a=Label(self.can[0],text="THONG TIN Giao vien")
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

        Button(self.can[1],text="ID",command=self.idc).place(x=10,y=0)
        Button(self.can[1],text="Name",command=self.name).place(x=50,y=0)
        Label(self.can[1],text="Choose").place(x=200,y=0)
        Button(self.can[1],image=self.hinh[0],command=self.src).place(x=0,y=225)
        self.update_class()

        A=Button(self.master,text = "Join class",width=17,height=5,bg="yellow")
        A.place(x=470,y=0)
        
        B=Button(self.master,text = "Create class",width=17,height=5,bg="blue",command=self.create_class)
        B.place(x=470,y=80)
        
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
    
    def create_class(self):
        create_class(Toplevel(),self.id)
    
    def update_class(self):
        b=len(self.arr_class)
        tx=10
        ty=20
        if self.sreach:
            if  self.sreach:
                for i in range(0,len(self.sreach)):
                    self.sreachL[i][0].destroy()
                    self.sreachL[i][1].destroy()
                    self.sreachR[i].destroy()
                self.sreach=[]
            
        if not self.Label[b-1][0]:
            for i in range(0,b):
                self.Label[i][0]=Label(self.can[1],text=self.arr_class[i][0])
                self.Label[i][1]=Label(self.can[1],text=self.arr_class[i][2])
                self.radi[i]=Radiobutton(self.can[1],variable=self.boo,value=self.arr_class[i][0])
                self.radi[i].invoke()
        else :
            for i in range(0,b):
                self.Label[i][1].place_forget()
                self.Label[i][0].place_forget()
                self.radi[i].place_forget()
        for i in range(0,b):
            self.Label[i][1].place(x=tx+40,y=ty)
            self.Label[i][0].place(x=tx,y=ty)
            self.radi[i].place(x=tx+190,y=ty)
            ty+=20

    def idc(self):
        quickSort(self.arr_class,self.Label,self.radi,0,len(self.arr_class)-1)
        self.pos=0
        print(self.boo.get())
        self.update_class()
    
    def  name(self):
        quickSort(self.arr_class,self.Label,self.radi,0,len(self.arr_class)-1,2)
        self.pos=2
        print(self.boo.get())
        self.update_class()

    def src(self):
        self.valueSrc=StringVar()
        if self.pos==0:
            self.valueSrc.set("Id")
        elif self.pos==2:
            self.valueSrc.set("Name")
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
                self.Label[i][1].place_forget()
                self.Label[i][0].place_forget()
                self.radi[i].place_forget()
        self.sreach=[]
        self.sreach=binarySearch(self.arr_class,0,len(self.arr_class)-1,self.valueSrc.get())
        print(self.valueSrc.get())
        print(self.sreach)
        print(self.arr_class)
        tx=10
        ty=20
        for i in range(0,len(self.sreach)):
            self.Label[i][0]=Label(self.can[1],text=self.arr_class[i][0])
            try:
                self.sreachL[i][0]
            except:
                self.sreachL.append([None,None])
                self.sreachR.append(None)
            self.sreachL[i][0]=Label(self.can[1],text=self.sreach[i][0])
            self.sreachL[i][1]=Label(self.can[1],text=self.sreach[i][2])
            self.sreachR[i]=Radiobutton(self.can[1],variable=self.boo,value=self.sreach[i][0])
            self.sreachR[i].invoke()
            self.sreachL[i][1].place(x=tx+40,y=ty)
            self.sreachL[i][0].place(x=tx,y=ty)
            self.sreachR[i].place(x=tx+190,y=ty)
            ty+=20

Open_S(Tk(),"1")