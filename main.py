
from panda import Panda 

char1 = Panda("Cooper" , "Age : 18 " , "favorite_food : Bamboo " , "Weight : 120 Kg " )
char2 = Panda("Daisy" , "Age : 13 ", "favorite_food : Leaves " , " Weight : 95 Kg ")
char3 = Panda("Bella" , "Age : 6 " , "favorite_food : stems ", "Weight : 100 Kg " )
char4 = Panda("Max" , "Age : 20 " , "favorite_food : shoots of various bamboo species " , "Weight : 70 Kg " )



print(char1.name )
print(char1.p_age())
print(char2.p_age())
print(char3.p_age())
print(char4.p_age())

print(char1.brief())
print(char2.brief())
print(char3.brief())
print(char4.brief())
