class Panda:

    def __init__(self, gender:str, age:int, country:str, caretaker:str):
        self.gender = gender
        self.setAge(age)
        self.country = country
        self.caretaker = caretaker
    
    def getAge(self):
        return self.__age
    
    def setAge(self, age:int):
        if not isinstance(age, int):
            raise ValueError("You must provide a number.")
        self.__age = age

    def brief(self):
        return f"The gender is: {self.gender} age: {self.getAge()}, lives in: {self.country}, taken care by: {self.caretaker}"
        