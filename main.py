from datetime import date
from PandaClass import Panda

panda1 = Panda("Lulu" , 170 ,110 , date.today())
panda2 = Panda("Amit" , 160 ,90 , date.today())
panda3 = Panda("Anita" , 176 ,150 , date.today())
panda4 = Panda("Mika" , 153 ,85 , date.today())

print(panda1.name)
print(panda1.mood() , panda1.Height())
print(panda2.mood() , panda2.Height())
print(panda3.mood() , panda3.Height())
print(panda4.mood() , panda4.Height())