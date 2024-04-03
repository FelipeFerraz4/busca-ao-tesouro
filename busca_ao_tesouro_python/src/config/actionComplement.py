from pygame.locals import *
import random
import copy

from src.graph.search import breadthFirstSearch, depthFirstSearch, searchVerticalEmpty
from src.config.button import *
from src.graph.read import graphRead
from src.graph.vertice import *
from src.config.screen import *
from src.graph.informateVertice import draw_informationVetices
from .draw_info_vertice import *
from src.character.monster import *
from src.character.weapon import *
# from .display import *

screen = createScreen()
backGround = createBackground()
graph = graphRead()

button_reset = create_button_reset()
button_next = create_button_next()
button_scape = create_button_scape()
button_combat = create_button_combat()
button_get = create_button_get()
button_release = create_button_release()
button_florest = create_button_florest()

def nextPosition(personVertice, verticeObjective, graph):
    # get the best neighbor of the character's current vertice
    bestNeighboringVertice = breadthFirstSearch(graph, graph[personVertice], graph[verticeObjective])
    neighboringList = copy.deepcopy(graph[personVertice].adjacentVertices)
    
    # 20% of being chosen the best vertice
    porcente = 6/10
    luckNumber = random.randint(0, len(neighboringList))

    # choosing the next vertice
    neighboringChoice = bestNeighboringVertice
    
    if luckNumber > int(len(neighboringList)*porcente):
        if bestNeighboringVertice in neighboringList:
            neighboringList.remove(bestNeighboringVertice)
        numberChoice = random.randint(0, len(neighboringList) - 1)
        neighboringChoice = neighboringList[numberChoice]
    
    return neighboringChoice

def newVerticeMonster(monsters, weapons):
    newVerticeEmpty = False
    newVertice = 0
    while newVerticeEmpty == False:
        newVertice = searchVerticalEmpty(graph, graph[random.randint(0, len(graph) - 1)], weapons)
        count = 0
        for elementMonster in monsters:
            if elementMonster.vertices == newVertice:
                count += 1
        if count == 0:
            newVerticeEmpty = True
    return newVertice
                      
def moviment_monster(graph, monsters, weapons):
    for item in monsters:
        vertice = searchVerticalEmpty(graph, graph[random.randint(0, len(graph) - 1)], weapons)
        monsterVertices = []
        for monster  in monsters:
            if monster.vertices == vertice:
                monsterVertices.append(monster)
        
        if len(monsterVertices) == 0:
            item.vertices = vertice
        elif len(monsterVertices) == 1:
            monsterEnemy = monsterVertices[0]
            if monsterEnemy.attack_points >= item.attack_points:
                item.health_points = 100
                monsterEnemy.take_damage(item.attack_points)
                item.vertices = newVerticeMonster(monsters, weapons)
            else:
                monsterEnemy.health_points = 100
                item.take_damage(monsterEnemy.attack_points)
                monsterEnemy.vertices = newVerticeMonster(monsters, weapons)
        else:
            monsterStrong = monsterVertices[0]
            monsterWeak = monsterVertices[1]
            for elementMonster in monsterVertices:
                if elementMonster.attack_points > monsterStrong.attack_points:
                    monsterStrong = elementMonster
                if elementMonster.attack_points < monsterWeak.attack_points:
                    monsterWeak = elementMonster
            monsterWeak.health_points = 100
            monsterWeak.vertices = newVerticeMonster(monsters, weapons)
            monsterStrong.take_damage(monsterWeak.attack_points)
            for elementMonster in monsterVertices:
                if elementMonster.index != monsterWeak.index != monsterStrong.index:
                    elementMonster.take_damage(monsterStrong.attack_points)
                    if elementMonster.health_points == 0:
                        elementMonster.health_points = 100
                    elementMonster.vertices = newVerticeMonster(monsters, weapons)
  
def update_treasure(person, weapons):
    if person.weapon != None:
        if person.treasure_percentage > (person.health-weapons[person.weapon].attack_bonus):
            person.treasure_percentage = (person.health-weapons[person.weapon].attack_bonus)
        if person.treasure_percentage < 0:
            person.treasure_percentage = 0
    else:
        if person.treasure_percentage > person.health:
            person.treasure_percentage = person.health
