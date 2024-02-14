class Panda:
    
    def __init__(self,name:str ,color:str ,age:int,gender:str):
        self.name = name 
        self.color = color
        self.age = age
        self.gender = gender
        
        
        
    def ageGroup(self):
        if self.age <=3 :
            print(f"{self.name} : in The Cub Stage")
        elif self.age >=4 or self.age <=6:
            print(f"{self.name}: in The Sub Adult Stage")
        else:
            print(f"{self.name}: in The Adult Stage")
            
    
    def nameLength(self):
        if len(self.name) <3 :
            print(f"{self.name} is a Short Length Name")
        elif len(self.name) <7 :
            print(f"{self.name} is a Normal Length Name")
        else:
            print(f"{self.name} is a long Length Name")
    
    
    
    
            