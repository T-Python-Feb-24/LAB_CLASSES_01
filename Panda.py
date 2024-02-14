class Panda:
    def __init__(self, name: str, age: int, gender: str, weight: float):
        self.name = name  # public
        self.age = age  # public
        self.gender = gender  # public
        self.__weight = weight  # private

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight: float):
        if not isinstance(weight, (int, float)):
            raise ValueError("Weight must be a number")
        self.__weight = weight

    def eat(self, food: str):
        return f"{self.name} is enjoying {food}!"

    def birthday(self):
       
        return f"{self.name} is {self.gender}! {self.name} now {self.age} years old."