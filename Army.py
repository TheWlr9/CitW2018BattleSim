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