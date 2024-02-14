from datetime import date

class Panda:

    def __init__(self, name:str , hight:float , weight:int , dudate:date ):
     self.name=name #public
     self.dudate=dudate #public
     self.hight=hight #public
     self.weight=weight #public
    
    def mood (self):
     return f"{self.name} he/she is not in the mood du date on : {self.dudate} "
    
    def Height (self):
      return f" \n{self.name} he/she is get this hight {self.hight} du date on : {self.dudate}\n"
    



    