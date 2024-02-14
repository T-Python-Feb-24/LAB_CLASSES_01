from PandaFile import Panda 

# Create 4 instances/objects of the class Panda
first = Panda("one", "black", 6,"F")
secound = Panda("second","wite",3,"M")
third = Panda("third","gray", 10,"M")
fourth =Panda("fourthPanda","brown",1,"F")


# print 1 attribute value,  and call the two methods on each instance. 
print("first instance age:",first.age)
print("second instance gender:",secound.gender)
print("third instance color:",third.color)
print("fourth insatnce name:", fourth.name)
print()

print ("Output of ageGroup Function:\n")
first.ageGroup()
secound.ageGroup()
third.ageGroup()
fourth.ageGroup()
print()

print ("Output of nameLength Function:\n")

first.nameLength()
secound.nameLength()
third.nameLength()
fourth.nameLength()

