from datetime import date

class Panda:
    def __init__(self, color:str ,Gender:str,behavior:str , date_birth:date):
        self.color= color
        self.Gender= Gender
        self.behavior=behavior
        self.date_birth= date_birth
    
    def describe_panda(self):
        return f"{self.color},{self.Gender},{self.behavior},{self.date_birth}"
    
    def behavior_panda(self):
        return f"{self.behavior}"
