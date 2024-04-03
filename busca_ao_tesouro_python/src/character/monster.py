
class Monster():
    def __init__(self, position, monster_type, vertices, health_points, attack_points):
        self.index = position 
        self.type = monster_type
        self.vertices = vertices
        self.health_points = health_points
        self.attack_points = attack_points


    def take_damage(self, damage):
        self.health_points -= damage
        if self.health_points < 0:
            self.healyh_points = 0

def isMonster(monsters, vertice):
    for monster in monsters:
        if monster.vertices == vertice:
            return True
    return False

def getMonster(monsters, vertice):
    for monster in monsters:
        if monster.vertices == vertice:
            return monster.index
    return -1