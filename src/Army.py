# LIBRAIRIES
from Soldier import Assassin, Knight, Ninja, Spartian
from Infrastructure import Bunker, Camp, Deposit, Hospital, Outpost

class Army():
    # ATTRIBUTS
    name = ""
    soldiers = []
    infrastructures = []
    maximumCost = 1000000
    maximumpopulation = 1000

    # CONSTRUCTOR
    def __init__(self, name):
        self.name = name
        print("Army " + name + " created")

    # METHODS
    # Added this method to control the formations
    def formation(self, formation):
        pass

    def checkCost(self):
        cost = -1
        return cost

    def checkPopulation(self):
        population = -1
        return population

    def createFromFile(self):
        pass