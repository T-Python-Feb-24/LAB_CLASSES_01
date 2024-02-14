from Panda import Panda
from datetime import date


def main() -> None:
    pd1 = Panda(name="Shadow", description="eat a lot until he get fat",
                birth_date=date(2020, 5, 18), gender="Male")

    pd2 = Panda("Lona", description="sleep a lot of time",
                birth_date=date(2021, 8, 3), gender="Female")

    pd3 = Panda("Alfred", description="So frindly",
                birth_date=date(2019, 12, 15), gender="Male")

    pd4 = Panda("Lilly", description="she Very feisty",
                birth_date=date(2022, 3, 10), gender="Female")

    pd1.print_info()
    print(f"{pd4.get_age()} years")
    pd4.set_birth_date(date(2022, 6, 10))


if __name__ == '__main__':
    main()
