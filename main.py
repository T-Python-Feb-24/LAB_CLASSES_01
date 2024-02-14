from panda import Panda

panda1 = Panda ("Aliuropoda melanoleuce", "Giant Panda", "White & Black", 90, "China")
panda2 = Panda ("Ailurus fulgens N", "Red Panda", "Red & Black", 5, "Nepal")
panda3 = Panda ("Ailurus fulgens B", "Red Panda", "Red & Black", 6, "Bhutan")
panda4 = Panda ("Aliuropoda melanoleuce qinlingensis", "Qinling Panda", "White & Brown", 42, "China")




print("------ identification Panda cards ------")
print("----------------------------------------")
print(f"         {panda1.panda_name}    ")
print("----------------------------------------")
panda1.identification_card()

print(f"            {panda2.panda_name}    ")
print("----------------------------------------")
panda2.identification_card()

print(f"            {panda3.panda_name}    ")
print("----------------------------------------")
panda3.identification_card()


print(f"   {panda4.panda_name}    ")
print("----------------------------------------")
print("* This is old card!!")
panda4.identification_card()

panda4.set_panda_weight(44)
print(f"* Last update(weight changed {panda4.get_panda_weight()} kg)")
panda4.identification_card()




