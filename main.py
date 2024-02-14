from class_panda import Panda

panda1 = Panda('Koko', 7, 'Male', 0)

panda2 = Panda('Lela', 5, 'Female',0)

panda1.set_panda_zone(1)
panda2.set_panda_zone(3)
print(f'This is about {panda1.name}: {panda1.panda_data()}')

