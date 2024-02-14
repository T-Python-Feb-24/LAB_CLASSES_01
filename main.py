from lab import Panda
from datetime import date

#Create 4 instances/objects of the class Panda
pa1=Panda("Black","male","docile overall and often lower their heads ",date(2023,12,1))
pa2=Panda("white","female","shade their faces with their front ",date.today())
pa3=Panda("white","male","attempt to conceal himselve when he come across a human for the first time",date(2022,11,4))
pa4=Panda("Black","female","alone",date(2021,8,13))

#print 1 attribute value
print(pa1.date_birth)

#and call the two methods on each instance (the first method). 
print(pa1.describe_panda())
print(pa2.describe_panda())
print(pa3.describe_panda())
print(pa4.describe_panda())

#the second method
print(pa1.behavior_panda())
print(pa2.behavior_panda())
print(pa3.behavior_panda())
print(pa4.behavior_panda())