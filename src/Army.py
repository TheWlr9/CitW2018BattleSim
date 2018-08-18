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
    def __init__(self, name, soldiers, infastructures, maxCost, maxPop):
        self.name = name
        self.soldiers= soldiers
        self.infastructures= infastructures
        maximumCost= maxCost
        maximumpopulation= maxPop
        print("Army " + name + " created")

    # METHODS
    # Added this method to control the formations
    def formation(self, formation):
        pass

    def checkCost(self):
        return cost

    def checkPopulation(self):
        return population

    def createFromFile(self):
        pass