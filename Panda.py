from datetime import date
from dateutil.relativedelta import relativedelta


class Panda:
    def __init__(self, name: str, description: str, birth_date: date, gender: str):
        self.__name: str = name
        self.__description: str = description
        self.__birth_date: date = birth_date
        self.__gender: str = gender

    def get_name(self) -> str:
        return self.__name

    def get_description(self) -> str:
        return self.__description

    def get_birth_date(self) -> date:
        return self.__birth_date

    def get_gender(self) -> str:
        return self.__gender

    def get_age(self):
        return relativedelta(date.today(), self.get_birth_date()).years

    def print_info(self):
        print(f'''
--------------------------------
The Panda info:
    Name: {self.get_name()}
    Age:  {self.get_age()}
    Gender: {self.get_gender()}
----------------------------------
 ''')

    def set_birth_date(self, birth_date):
        if not isinstance(birth_date, date):
            raise TypeError("birth_date must be date")
        return birth_date

    def set_gender(self, gender: str):
        match gender.capitalize():

            case "Male" | "Female":
                self.__gender = gender
                return
            case _:
                raise ValueError("gender must be Male or Female")
