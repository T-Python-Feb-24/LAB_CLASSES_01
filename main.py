from panda import Panda
panda1= Panda ("name:losi" ,"age:5","Description:Giant pandas have a distinctive black and white coat", " gender:male")
panda2= Panda("name:kisi","age:3","Description:black fur around their eyes and on their ears muzzle legs and shoulders","gender:female")
panda3= Panda("name:black","age:4","Description:wooly coat helps to keep them warm in their cool mountain homes","gender:male")
panda4= Panda("name:poa" ,"age:5","Description:Adult pandas are about 150cm from nose to rump  with a 10-15cm tail","gender:female")


print(panda1.age)
print(panda1.p_name())
print(panda2.p_name())
print(panda3.p_name())
print(panda4.p_name())

print(panda1.brief())
print(panda2.brief())
print(panda3.brief())
print(panda4.brief())