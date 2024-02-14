from Panda import Panda

panda1 = Panda("Pande", 5, "Male", 250)

panda2 = Panda("Sali ", 6, "Female", 200)

panda3 = Panda("Soma", 4, "Female", 180)

panda4 = Panda("Pandiju", 7, "Male", 300)


print(panda1.name)
print(panda1.eat("Bamboo"))
print(panda1.birthday())
print("_"*30)

print(panda2.name)
print(panda2.eat("Leaves"))
print(panda2.birthday())
print("_"*30)

print(panda3.name)
print(panda3.eat("Shoots"))
print(panda3.birthday())
print("_"*30)

print(panda4.name)
print(panda4.eat("Bamboo and Fruits"))
print(panda4.birthday())
print("_"*30)