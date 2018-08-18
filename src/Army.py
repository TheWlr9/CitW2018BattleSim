# LIBRAIRIES
from Soldier import Assassin, Knight, Ninja, Spartian
from Infrastructure import Bunker, Camp, Deposit, Hospital, Outpost
from Equipment import Dog, Horse, Tiger, Boat, Car, Plane

class Army():
    # ATTRIBUTS
    name = ""
    soldiers = []
    infrastructures = []
    equipments = []
    maximumCost = 1000000
    maximumpopulation = 1000

    # CONSTRUCTOR
    def __init__(self, name):
        self.name = name
        print("Army " + name + " created")

    # METHODS
    def checkCost(self):
        pass

    def checkPopulation(self):
        pass

    def createFromFile(self):
        pass