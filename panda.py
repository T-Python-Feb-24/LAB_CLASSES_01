class Panda:
     #
     def __init__ (self , name:str,age:float,Description:str,gender:str):
      self. name= name 
      self. age= age
      self. Description= Description
      self. gender = gender
      #
     def p_name(self):
      return self.name
          
     def brief(self):
        return f"{self.name}, {self.age}, {self.Description},{self.gender}"