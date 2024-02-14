class Panda:
    def __init__(self, gender:str, weight:float, height:float, type:str):
        self.gender = gender  
        self.set_weight(weight) 
        self.set_height(height)  
        self.type = type  

    def get_weight(self):
        return self.weight

    def set_weight(self, weight: float):
        
        if weight is None:
            raise ValueError("You must provide weight")
        self.weight = weight 

    def get_height(self):
        return self.height
    
    def set_height(self, height:float):
        if height is None:
            raise ValueError("You must provide height ")
        self.height = height
        
    def brief(self):
        return f"The Male is: {self.gender} weighs {self.get_weight()} and is {self.get_height()} units tall. It is of type {self.type}."
