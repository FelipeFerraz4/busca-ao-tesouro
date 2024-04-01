from time import sleep
import pygame
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

screen = createScreen()
backGround = createBackground()
graph = graphRead()
button_reset = create_button_reset()
button_next = create_button_next()
button_scape = create_button_scape()
button_combat = create_button_combat()

pygame.font.init()
fonte = pygame.font.get_default_font()
fontesys = pygame.font.SysFont(fonte, 40)

class Game():
    def __init__(
        self, 
        verticeObjective=3, 
        time=0, 
        startTime=pygame.time.get_ticks(), 
        statusGame=-1, 
        end=False,
        combatMenu=False,
        ):
      self.verticeObjective = verticeObjective
      self.time = time
      self.startTime = startTime
      self.statusGame = statusGame
      self.end = end
      self.combatMenu = combatMenu
      self.combatRound = 3

def gameOn(game, person, monsters):
    if game.statusGame > -1:
        res = 0
        
        if game.combatMenu == False:
            res =  display_default(game, monsters, person)
        else:
            res = display_combat(game, monsters, person)
        
        if res != 0:
            return res
        
        if message_end(game, person) == 2:
            return 2
        return 0
    else:
        return startMessage(game.statusGame, game.startTime, monsters)
    

def nextPosition(personVertice, verticeObjective):
    # get the best neighbor of the character's current vertice
    bestNeighboringVertice = breadthFirstSearch(graph, graph[personVertice], graph[verticeObjective])
    neighboringList = copy.deepcopy(graph[personVertice].adjacentVertices)
    
    # 20% of being chosen the best vertice
    porcente = 3/10
    luckNumber = random.randint(0, len(neighboringList))

    # choosing the next vertice
    neighboringChoice = bestNeighboringVertice
    
    if luckNumber > int(len(neighboringList)*porcente):
        neighboringList.remove(bestNeighboringVertice)
        numberChoice = random.randint(0, len(neighboringList) - 1)
        neighboringChoice = neighboringList[numberChoice]
    
    return neighboringChoice

def step(personVertice, nextVertice):
    #change the person's vertice
    graph[personVertice].person = False
    graph[nextVertice].person = True
    
def startMessage(statusGame, startTime, monsters):
    draw_backGround(backGround, screen)
    draw_edges(graph, screen)
    draw_vertices(graph, screen)
    draw_informationVetices(graph, screen, monsters)
    
    if statusGame == -1:
        txttela = fontesys.render('Prepare-se, a ilha está a vista', 1, (255,255,255))
    elif statusGame == -2:
        txttela = fontesys.render('Desvende segredos ocultos e tesouros.', 1, (255,255,255))
    elif statusGame == -3:
        txttela = fontesys.render('Uma jornada emocionante começa agora!', 1, (255,255,255))
    screen.blit(txttela, (180, 280))
    count_timer = pygame.time.get_ticks()
    if startTime + 1000 <= count_timer <= startTime + 2000:
        return -2
    elif startTime + 2000 < count_timer <= startTime + 3000:
        return -3
    elif startTime + 3000 < count_timer:
        return 0
    return -1

def display_default(game, monsters, person):
    global graph
    draw_backGround(backGround, screen)
    draw_edges(graph, screen)
    draw_vertices(graph, screen)
    draw_informationVetices(graph, screen, monsters)
    person.draw_explorer_info(fontesys, screen)
    personVertice = depthFirstSearch(graph, graph[0])
    
    person.get_treasure(graph, personVertice)
    
    if button_reset.draw(screen):
        graph = graphRead()
        sleep(0.1)
        return 3
    if button_next.draw(screen) and game.end == False:
        nextVertice = nextPosition(personVertice, game.verticeObjective)
        step(personVertice, nextVertice)
        if personVertice == 3:
            graph[3].treasure = False
        if nextVertice == 3:
            return 1
        if game.verticeObjective == 10 and nextVertice == 10:
            return 2
        game.time += 1
        damage_biome(graph, nextVertice, person)
        if isMonster(monsters, nextVertice):
            game.combatMenu = True
            game.startTime = pygame.time.get_ticks()
        sleep(0.1)
        print('next')
    return 0

def message_end(game, person):
    if game.time > 120:
        txttela = fontesys.render('Game Over, tempo esgotado', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        return 2
    if person.health == 0:
        txttela = fontesys.render('Game Over, muito danano', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        return 2
    if game.statusGame == 2:
        txttela = fontesys.render('Parabéns, fase completa!', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        return 2
    return 0


def display_combat(game, monsters, person):
    global graph
    draw_backGround(backGround, screen)
    draw_edges(graph, screen)
    draw_vertices(graph, screen)
    draw_informationVetices(graph, screen, monsters)
    person.draw_explorer_info(fontesys, screen)
    
    personVertice = depthFirstSearch(graph, graph[0])
    monster = monsters[getMonster(monsters, personVertice)]
    
    if game.combatRound == 3:
        txttela = fontesys.render('Monstro, escolha combate ou fuga', 1, (255,255,255))
        screen.blit(txttela, (180, 280))
    elif game.combatRound == 2:
        txttela = fontesys.render('Segundo turno, escolha combate ou fuga', 1, (255,255,255))
        screen.blit(txttela, (180, 280))
    elif game.combatRound == 1:
        txttela = fontesys.render('Terceiro turno, escolha combate ou fuga', 1, (255,255,255))
        screen.blit(txttela, (180, 280))

    
    if button_scape.draw(screen):
        person.take_damage(monster.attack_points)
        if person.treasure_percentage > person.health:
            person.treasure_percentage = person.health
            
        game.combatMenu = False
        game.combatRound = 3
        
        nextVertice = nextPosition(personVertice, game.verticeObjective)
        step(personVertice, nextVertice)
        sleep(0.2)
        print('scape')
        
        if nextVertice == 3:
            return 1
        if game.verticeObjective == 10 and nextVertice == 10:
            return 2
    
    if button_combat.draw(screen):
        print(len(graph))
        if game.combatRound == 3:
            person.take_damage(monster.attack_points)
            monster.take_damage(person.attack)
            
            if monster.health_points == 0:
                monster.health_points = 100
                monster.vertices = searchVerticalEmpty(graph, graph[random.randint(0, len(graph))])
                game.combatMenu = False
                game.combatRound = 3
            
            game.combatRound = 2
        elif game.combatRound == 2:
            person.take_damage(monster.attack_points)
            monster.take_damage(person.attack)
            
            if monster.health_points == 0:
                monster.health_points = 100
                monster.vertices = searchVerticalEmpty(graph, graph[random.randint(0, len(graph))])
                game.combatMenu = False
                game.combatRound = 3
            
            game.combatRound = 1
        elif game.combatRound == 1:
            person.take_damage(monster.attack_points)
            monster.take_damage(person.attack)
            
            if monster.health_points == 0:
                monster.health_points = 100
                monster.vertices = searchVerticalEmpty(graph, graph[random.randint(0, len(graph)) - 1])
                game.combatMenu = False
                game.combatRound = 3
            
            game.combatMenu = False
            game.combatRound = 3
            nextVertice = nextPosition(personVertice, game.verticeObjective)
            step(personVertice, nextVertice)        
            
        print(game.combatRound)
        nextVertice = nextPosition(personVertice, game.verticeObjective)
        if nextVertice == 3:
            return 1
        if game.verticeObjective == 10 and nextVertice == 10:
            return 2

        print('combat')
        
    return 0
    