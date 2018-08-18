# LIBRAIRIES


####################################################
#       EQUIPMENT
####################################################
class Equipment():
    # ATTRIBUTS
    

    # CONSTRUCTOR
    def __init__(self):
        print("Equipment created")

    # METHODS

####################################################
#       ANIMALS
####################################################
class Animal(Equipment):
    # ATTRIBUTS
    

    # CONSTRUCTOR
    def __init__(self):
        pass
    # METHODS


class Horse(Animal):
    # ATTRIBUTS
    

    # CONSTRUCTOR
    def __init__(self):
        print("Horse created")
    # METHODS


class Dog(Animal):
    # ATTRIBUTS
    

    # CONSTRUCTOR
    def __init__(self):
        print("Dog created")
    # METHODS


class Tiger(Animal):
    # ATTRIBUTS
    

    # CONSTRUCTOR
    def __init__(self):
        print("Tiger created")
    # METHODS


####################################################
#       VEHICULES
####################################################
class Vehicule(Equipment):
    # ATTRIBUTS
    # Scale from 0-10
    speed= 0
    armor= 0
    attackPower= 0
    

    # CONSTRUCTOR
    def __init__(self):
        print("Vehicule created")

    # METHODS


class Car(Vehicule):
    # ATTRIBUTS
    

    # CONSTRUCTOR
    def __init__(self):
        print("Dog created")
        super.speed= 8
        super.armor= 5
        super.attackPower= 1
    # METHODS


class Plane(Vehicule):
    # ATTRIBUTS
    

    # CONSTRUCTOR
    def __init__(self):
        print("Dog created")
        super.speed= 10
        super.armor= 4
        super.attackPower= 3
    # METHODS


class Boat(Vehicule):
    # ATTRIBUTS
    

    # CONSTRUCTOR
    def __init__(self):
        print("Dog created")
        super.speed= 5
        super.armor= 4
        super.attackPower= 5
    # METHODS