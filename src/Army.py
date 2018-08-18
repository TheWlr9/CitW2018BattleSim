# LIBRAIRIES
from Soldier import Assassin, Knight, Ninja, Spartian
from Infrastructure import Bunker, Camp, Deposit, Hospital, Outpost

class Army():
    # ATTRIBUTS
    name = ""
    # This stores all the soldier types and quantity
    soldiers = []
    infrastructures = []

    # CONSTRUCTOR
    def __init__(self, name):
        self.name = name
        print("Army " + name + " created")

    # METHODS

    def checkCost(self):
        cost = -1
        return cost

    def checkPopulation(self):
        population = -1
        return population

    def createFromFile(self, fileName):
        pass