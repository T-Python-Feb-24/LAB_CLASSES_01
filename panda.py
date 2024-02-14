

class Panda :
    def __init__ (self, name:str , age:int , favorite_food: str , weight:int) :
      self.name = name
      self.age = age
      self.favorite_food = favorite_food
      self.weight = weight

    def p_age(self):
       return self.age
    
    def brief(self):
       return f"{self.name}is a Panda bear,{self.age},{self.favorite_food}and the {self.weight}"
