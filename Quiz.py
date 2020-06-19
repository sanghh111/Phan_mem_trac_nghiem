from Question import *

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

    def exportFIle(self):
        namefile="quiz/"+self.content+".quiz"
        out=open(namefile,"w")
        