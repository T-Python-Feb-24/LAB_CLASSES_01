class Panda:
    def __init__(self,size:str,weight:str,name:str,age:str,food:str):
        self.size=size
        self.weight=weight
        self.name=name
        self.__age=age
        self.food=foodla
    def Panda(self):
        return f"{self.size}, {self.weight},{self.name}"
    
    def feature(self):
        return f"{self.size},{self.weight}"
    
    def eat(self, food): 
        return f"{self.name},is eating{food}"
    
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    
        