from tkinter import *
from PIL import Image, ImageTk

class Quiz(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.master=master
        self.tool_1=[]
        self.load=[]
        self.hinh=[]
        self.Quiz=None
        self.tool_4=None
        self.choices=0
        self.Label=[]
        self.name=[]
        self.content=[]
        self.bool=[]
        self.choice=[]
        self.Page=0
        self.display()
    
    def display(self):
        self.master.geometry("400x400")
        self.load.append(Image.open("Image\\quizz200x100.png"))
        self.hinh.append(ImageTk.PhotoImage(self.load[0]))
        self.img=Label(self.master,image=self.hinh[0])#0 la Question200x100
        self.img.pack()
        self.img.place(x=100,y=0)
        self.a=Button(self.master,text=">",height=1,width=1,command=self.tool)
        self.a.pack()
        self.a.place(x=100,y=100)
        self.Button_1=Button(self.master,text="nextPage",command=self.nextpage)
        self.Button_1.pack()
        self.Button_1.place(x=340,y=375)
        self.Button_2=Button(self.master,text="previousPage",command=self.previousPage)
        self.Button_2.pack()
        self.Button_2.place(x=0,y=375)
        self.master.mainloop()

    def tool(self):
        if not self.tool_1:
            if self.Quiz:
                self.tool_1=Button(self.master,text="-",height=1,width=1,bg="red",command=self.creat_newQuiz )
            else:
                self.tool_1=Button(self.master,text="+",height=1,width=1,bg="red",command=self.creat_newQuiz )
            self.tool_1.pack()
            self.tool_1.place(x=115,y=100)
            self.tool_3=Button(self.master,text="C",height=1,width=1,bg="red",command=self.toolChoice)
            self.tool_3.pack()
            self.tool_3.place(x=130,y=100)
            self.rech=None
            self.a.config(text="<")
        else :
            self.tool_1.destroy()
            self.tool_3.destroy()
            self.tool_1=None
            self.tool_3=None
            self.a.config(text=">")
            if self.tool_4:
                self.tool_4.destroy()
                self.tool_4=None
                self.tool_5.destroy()
                self.tool_5=None
            
    def creat_newQuiz(self):
        if not self.Quiz:
            try:
                self.name[self.Page]
            except:
                self.name.append(StringVar())
            print(self.name)
            self.Quiz=Entry(self.master,textvariable=self.name[self.Page])
            self.Quiz.pack()
            self.Quiz.place(x=200,y=100)
            self.tool_2=Button(self.master,text="OK",command=self.getNameQuiz)
            self.tool_2.pack()
            self.tool_2.place(x=300,y=100)
            self.tool_1.config(text="-")

    def getNameQuiz(self):
        # print(self.name.get())
        self.Quiz.destroy()
        self.Quiz=None
        self.tool_2.destroy()
        self.tool_2=None
        self.Label.append(Label(self.master,textvariable=self.name[self.Page],font=("Helvetica", 20)))
        self.Label[self.Page].pack()
        self.Label[self.Page].place(x=200,y=150,anchor="center")
        if self.tool_1:
            self.tool_1.config(text="+")

    def toolChoice(self):
        if not self.tool_4:
            self.tool_4=Button(self.master,text="+",bg="red",command=self.addChoice)
            self.tool_4.pack()
            self.tool_4.place(x=145,y=100)
            self.tool_5=Button(self.master,text="-",bg="red",command=self.removeChoice)
            self.tool_5.pack()
            self.tool_5.place(x=160,y=100)
        else:
            self.tool_4.destroy()
            self.tool_4=None
            self.tool_5.destroy()
            self.tool_5=None

    def addChoice(self):
        try :
            self.choice[self.Page]
        except :
            self.choice.append([])
            self.content.append([])
            self.bool.append([])
        try :
            self.content[self.Page][self.choices]
        except :
            self.content[self.Page].append(StringVar())
            self.bool[self.Page].append(BooleanVar())
            print(self.content)
            self.ch=None
        if not self.ch:
            self.ch=Entry(self.master,textvariable=self.content[self.Page][self.choices])
            self.ch.pack()
            self.ch.place(x=200,y=100)
            self.tool_6=Button(self.master,text="OK",command=self.addChoiceS)
            self.tool_6.pack()
            self.tool_6.place(x=300,y=100)
        else:
            self.ch.destroy()
            self.tool_6.destroy()
            self.ch=None
            self.tool_6=None
        pass

    def addChoiceS(self):
        toadoY=150+30*self.choices
        self.ch.destroy()
        self.tool_6.destroy()
        self.ch=None
        self.tool_6=None
        print(self.bool)
        self.choice[self.Page].append(Checkbutton(self.master,
                                        textvariable=self.content[self.Page][self.choices],
                                        variable=self.bool[self.Page][self.choices]
                                        ))
        self.choice[self.Page][self.choices].pack( anchor = W)
        self.choice[self.Page][self.choices].place(x=30,y=toadoY)
        self.choices+=1
    
    def removeChoice(self):
        if self.choices>0 and not self.rech:
            self.int=IntVar()
            self.rech=Entry(self.master,textvariable=self.int)
            self.rech.pack()
            self.rech.place(x=200,y=100)
            self.tool_7=Button(self.master,text="OK",command=self.removeChoiceS)
            self.tool_7.pack()
            self.tool_7.place(x=300,y=100)
        elif self.rech:
            self.rech.destroy()
            self.rech=None
            self.tool_7.destroy()
            self.tool_7=None

    def removeChoiceS(self):
        self.rech.destroy()
        self.rech=None
        self.tool_7.destroy()
        self.tool_7=None
        j=0
        for i in self.choice[self.Page]:
            if j==self.int.get():
                i.destroy()
                self.choice[self.Page].remove(i)
            j+=1
        j=0
        for i in self.content[self.Page]:
            if j==self.int.get():
                self.content[self.Page].remove(i)
            j+=1
        j=0
        for i in self.bool[self.Page]:
            if j==self.int.get():
                self.bool[self.Page].remove(i)
            j+=1
        self.choices-=1
        self.updateC()
    
    def updateC(self):
        j=0
        for i in self.choice[self.Page]:
            toadoY=150+30*j
            i.place(x=30,y=toadoY)
            j=j+1
        self.choices=j
    def nextpage(self):
        if self.choice:
            for i in self.choice[self.Page]:
                i.pack_forget()
                i.place_forget()
            self.Label[self.Page].pack_forget()
            self.Label[self.Page].place_forget()
            self.Page+=1
            try :
                self.choice[self.Page]
            except :
                self.choice.append([])
                self.content.append([])
                self.bool.append([])
            self.choices=0


    def previousPage(self):
        if self.Page>=1:
            self.Page-=1
            self.updateC()
            self.Label[self.Page].pack()
            self.Label[self.Page].place(x=200,y=150,anchor="center")
App=Quiz(Tk())