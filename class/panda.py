class Panda:
    def __init__(self, name, age, weight, food,sleep_time):
        self.name = name
        self.age = age
        self.weight = weight
        self.food = food
        self.sleep_time= sleep_time

    def food_weight(self):
        print(f"this is panda {self.name}")
        print(f"{self.name} is eating {self.food}, and weight about {self.weight}KG.")

    def old_sleep(self):
        print(f"{self.name} is {self.age} years old, and sleeping for {self.sleep_time} hours.")
    print("-"*30)