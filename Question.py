from choice import *
class Question:
    def __init__(self,content="",Type=False):
        self.content=content
        self.Type=Type
        self.choice=[]
    def addChoice(self,choice):
        if self.Type==False:
            if(choice.get_answer()==True):
                for a in self.choice:
                    if a.get_answer()==True:
                        a.set_answer(False)
        self.choice.append(choice)

    def removeChoice(self,pos):
        i=1
        for a in self.choice:
            if(i==pos):
                self.choice.remove(a)
                return
            i+=1

    def getContent(self):
        return self.content

    def getChoice(self):
        return self.choice