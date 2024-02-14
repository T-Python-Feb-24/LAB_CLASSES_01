from lab10 import Panda
# Create four instances of the Panda class

# Note: gander by default 'unknown'
panda1=Panda(100,10,120)
panda2=Panda(98,11,112)
panda3=Panda(98,6,132)
panda4=Panda(98,7,105)

# Print the value of one attribute
print(panda1.gander)

# Call the two methods on each instance
panda2.set_panda_gander("female")
print(panda2.get_panda_gander())

panda3.set_panda_gander("male")
print(panda3.get_panda_gander())

panda4.set_panda_gander("female")
print(panda4.get_panda_gander())























# panda2.set_panda_gander("female")
# panda3.set_panda_gander("female")
# panda4.set_panda_gander("male")