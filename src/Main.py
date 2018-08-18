from Army import Army

print("Welcome to the Battle Simulation !\n")

army1Name= input("First army?")
army2Name= input("Second_army?")

army1 = Army(army1Name)
army2 = Army(army2Name)



def createArmy():
    # Where you can create your own army type.
    pass

def simulate():
    while(army1.checkPopulation>0 and army2.checkPopulation>0):
        pass # Put the simulation code here
    if(army1.checkPopulation<=0):
        print(army2Name+" wins!")
    else:
        print(army1Name+" wins!")