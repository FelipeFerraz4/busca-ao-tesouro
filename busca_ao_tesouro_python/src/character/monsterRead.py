from .monstersList import monsters
from .monster import Monster

def monsterRead():
    monster = []
    for element in monsters:
        monster.append(Monster(element[0], element[1],element[2],element[3], element[4]))
    return monster