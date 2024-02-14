from panda import  Panda

p1 = Panda('Pandora', 'Giant Panda', 20, 'Bamboo')
p2 = Panda('Apple', 'Red Panda', 10, 'Bamboo')
p3 = Panda('Charlie', "Grizzled Giant Panda", 5, 'Bamboo')
p4 = Panda('Brown Panda', 'Qinling Panda', 20, "Bamboo")

print("-------- Panda Types ---------")
print("Type: ",p1.type, ", Average Age: ", p1.get_age())
print("Type: ",p2.type, ", Average Age: ", p2.get_age())
print("Type: ",p3.type, ", Average Age: ", p3.get_age())
print("Type: ",p4.type, ", Average Age: ", p4.get_age())

print(p1.panda_info())
print(p2.panda_info())
print(p3.panda_info())
print(p4.panda_info())

print('\nUpdate Age value of the gaint panda')
p1.set_age('6')