from lab10 import Panda

try:
    panda1 = Panda(gender="Female", weight=150, height=50, type="red")
    Panda2 = Panda(gender="male", weight=100, height=60, type="red")
    Panda3 = Panda(gender="Female", weight=200, height=55, type="black")
    Panda4 = Panda(gender="male", weight=130, height=68, type="black")
    print(panda1.brief())
    print(Panda2.brief())
    print(Panda3.brief())
    print(Panda4.brief())
except Exception as e:
    print(e)