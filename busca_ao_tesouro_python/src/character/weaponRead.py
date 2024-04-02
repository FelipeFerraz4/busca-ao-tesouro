from .weaponList import weapons
from .weapon import Weapon

def weaponsRead():
    weapon = []
    for element in weapons:
        weapon.append(Weapon(element[0], element[1], element[2], element[3]))
    return weapon