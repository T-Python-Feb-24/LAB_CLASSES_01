class Panda:

    def __init__(self, panda_name:str, panda_type:str, panda_fur:str, panda_weight:int, live_in:str):
        self.panda_name = panda_name
        self.panda_type = panda_type
        self.panda_fur = panda_fur
        self.__panda_weight = panda_weight
        self.live_in = live_in

    def get_panda_weight(self):
        return self.__panda_weight

    def set_panda_weight(self, panda_weight:int):
        try:
            if not isinstance(panda_weight, int):
                raise ValueError("Invalid value. Only numbers are allowed.")
            self.__panda_weight = panda_weight
        except ValueError as e:
            print(e)

    def identification_card(self):
        print(f"- Type: {self.panda_type}")
        print(f"- Fur: {self.panda_fur}")
        print(f"- Weight: {self.get_panda_weight()} kg")
        print(f"- Live in: {self.live_in}")
        print("----------------------------------------")


