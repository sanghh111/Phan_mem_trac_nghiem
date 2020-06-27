from changeinfoT import*
class Open_S(Frame):
    def __init__(self,master,id):
        Frame.__init__(self,master)
        self.master=master
        self.can=[]
        self.id=id
        self.con,self.cur=connect_DB("Sinhvien.db")
        self.arr_info=Select_IT(self.cur,self.id)
        self.display()

    def display(self):
        self.master.geometry("600x400")

        self.can.append(Canvas(self.master,height=250,width=200,bg="white"))
        self.can[0].pack()
        self.can[0].place(bordermode=OUTSIDE,x=0,y=0)
        self.frame=Frame(self.master,height=250,width=250)
        self.frame.pack(expand=True,fill=BOTH)
        self.frame.place(x=200,y=0)
        self.can.append(Canvas(self.frame,height=250,width=250,bg="gray",scrollregion=(0,0,500,500)))
        self.Xbar=Scrollbar(self.frame,command=self.can[1].xview,orient=HORIZONTAL)
        self.Xbar.pack(side=BOTTOM,fill=X)
        self.Ybar=Scrollbar(self.frame,command=self.can[1].yview)
        self.Ybar.pack(side=RIGHT,fill=Y)
        self.can[1].create_text(300,300,text="Hello",fill="Blue")
        self.can[1].config(xscrollcommand=self.Xbar.set,yscrollcommand=self.Ybar.set)
        self.can[1].pack(expand=True,fill=BOTH)
        
        #LABEL INFO
        a=Label(self.can[0],text="THONG TIN SINH VIEN")
        a.place(x=35,y=5)
        #ID
        self.ID1=Label(self.can[0],text="ID")
        self.ID1.place(x=0,y=35)
        self.ID2=Label(self.can[0],text=self.arr_info[0])
        self.ID2.place(x=50,y=35)
        #Name
        self.Name1=Label(self.can[0],text="Name")
        self.Name1.place(x=0,y=65)
        self.Name2=Label(self.can[0],text=self.arr_info[2])
        self.Name2.place(x=50,y=65)
        #Class        
        self.Class_1=Label(self.can[0],text="Class")
        self.Class_1.place(x=0,y=95)
        self.Class_2=Label(self.can[0],text=self.arr_info[1])
        self.Class_2.place(x=50,y=95)
        #Birthday
        self.birth1=Label(self.can[0],text="Birthday")
        self.birth1.place(x=0,y=125)
        self.birth2=Label(self.can[0],text=self.arr_info[3])
        self.birth2.place(x=50,y=125)
        #Gender
        self.Gender1=Label(self.can[0],text="Gender")
        self.Gender1.place(x=0,y=155)
        self.Gender2=Label(self.can[0],text=self.arr_info[4])
        self.Gender2.place(x=50,y=155)
        #Phone
        self.Phone1=Label(self.can[0],text="Phone")
        self.Phone1.place(x=0,y=185)
        self.Phone2=Label(self.can[0],text=self.arr_info[5])
        self.Phone2.place(x=50,y=185)
        #Email
        self.Email1=Label(self.can[0],text="Email")
        self.Email1.place(x=0,y=215)
        self.Email2=Label(self.can[0],text=self.arr_info[6])
        self.Email2.place(x=50,y=215)

        A=Button(self.master,text = "Join class",width=17,height=5,bg="yellow")
        A.place(x=470,y=0)
        
        B=Button(self.master,text = "Resign class",width=17,height=5,bg="blue")
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