class choice:
    def __init__(self,content="",answer=False):
        self.content=content
        self.answer=answer
    
    def set_content(self,content):
        self.content=content

    def set_answer(self,answer):
        self.answer=answer

    def get_choice(self):
        return(self.content,self.answer)

    def get_answer(self):
        return self.answer