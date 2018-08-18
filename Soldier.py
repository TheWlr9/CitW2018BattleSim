# LIBRAIRIES
from Weapon import Weapon

class Soldier():
    # ATTRIBUTS
    name = ""
    location = (0,0)
    speed = 0
    armor = 0
    life = 0
    weapon = None

    # CONSTRUCTOR
    def __init__(self):
        print("Soldier created")

    # METHODS