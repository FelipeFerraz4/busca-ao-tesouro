class Weapon:
    def __init__(self, index, attack_bonus, vertices, name):
        self.index = index
        self.attack_bonus = attack_bonus 
        self.remaining_usage = 3
        self.vertices = vertices
        self.name = name

def isWeapon(weapons, vertice):
    for itemWeapon in weapons:
        if vertice == itemWeapon.vertices:
            return True
    return False

def getWeapon(weapons, vertice):
    for itemWeapon in weapons:
        if vertice == itemWeapon.vertices:
            return itemWeapon.index
    return 0