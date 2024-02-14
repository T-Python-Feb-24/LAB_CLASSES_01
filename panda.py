class Panda:
    def __init__(self, name:str, type:str, age:int, food:str):
        self.name = name
        self.type = type
        self.__age = age
        self.food = food
    
    def get_age(self):
         return self.__age
     
    def set_age(self, age:int):
        try:
            if not isinstance(age, int):
                raise ValueError("*Invalid Value: Age must be an integer*")
            self.__age = age
        except Exception as e:
            print(e)
    
    def panda_info(self):
        print("-----------------------------")
        print("-------- Panda Info. --------")
        return f"Name: {self.name}. \nType: {self.type}. \nAverage Age: {self.get_age()}  years. \nFavorite Food: {self.food}."