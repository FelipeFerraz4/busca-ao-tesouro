from monsterRead import monsterRead

class Monster():
    def __init__(self, monster_type, vertices, health_points, attack_points):
        self.type = monster_type
        self.vertices = vertices
        self.health_points = health_points
        self.attack_points = attack_points

def createMonster():
    firstMonsters = monsterRead()
    return firstMonsters

def take_damage(self, damage):
    self.health_points -= damage
    if self.health_points < 0:
        self.healyh_points = 0
