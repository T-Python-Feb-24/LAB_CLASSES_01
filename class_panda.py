class Panda:

    def __init__(self, name:str,age:int, gender:str, zone:int):
        self.name = name
        self.age = age
        self.gender = gender
        self.set_panda_zone(zone)
    
    
    def get_panda_zone(self):
        return self.__zone

    def set_panda_zone(self, zone:int):
        if not isinstance(zone, int):
            raise ValueError("you must enter an int")
        self.__zone = zone 
    
    def panda_data(self):
        return f"Panda's Name Is: {self.name}, And Age Is: {self.age}, And the Zone Is: {self.get_panda_zone()}"

        