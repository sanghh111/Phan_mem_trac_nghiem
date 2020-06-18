from Question import *
from choice import *

class Quiz:
    def __init__(self,content="",duration=0):
        self.content=content
        self.duration=duration
        self.Ques=[]

    def addQuestion(self,question):
        self.Ques.append(question)

    def removeQuestion(self,pos):
        i=1
        for a in self.Ques:
            if(i==pos):
                self.Ques.remove(a)
                return
            i+=1

    def getQues(self):
        return self.Ques        

q=Quiz("test nhanh",0)
Q=Question("2+2",0)
C=choice("4",1)
Q.addChoice(C)
q.addQuestion(Q)
for i in q.getQues():
    print(i.getContent())
    for j in i.getChoice():
        print(j.get_choice())