import pygame
from pygame.locals import *
import random
import copy

from src.graph.search import breadthFirstSearch, depthFirstSearch
from src.config.button import *
from src.graph.read import graphRead
from src.graph.vertice import *
from src.config.screen import *
from .biome import *

screen = createScreen()
backGround = createBackground()

graph = graphRead()
button_start = create_button_reset()
button_next = create_button_next()

biome = create_biome()
BiomeType = 0

pygame.font.init()
fonte = pygame.font.get_default_font()
fontesys = pygame.font.SysFont(fonte, 40)  

def gameOn(verticeObjective, end, statusGame, startTime):
    if statusGame > -1:
        global graph
        draw_backGround(backGround, screen)
        draw_edges(graph, screen)
        draw_vertices(graph, screen)
        draw_biomes(biome, screen, BiomeType)
        if button_start.draw(screen):
            graph = graphRead()
            return 3
        if button_next.draw(screen) and end == False:
            personVertice = depthFirstSearch(graph, graph[0])
            nextVertice = nextPosition(personVertice, verticeObjective)
            step(personVertice, nextVertice)
            if nextVertice == 3:
                return 1
            if verticeObjective == 10 and nextVertice == 10:
                return 2
            print('next')
        return 0
    else:
        return startMessage(statusGame, startTime)
def nextPosition(personVertice, verticeObjective):
    # get the best neighbor of the character's current vertice
    bestNeighboringVertice = breadthFirstSearch(graph, graph[personVertice], graph[verticeObjective])
    neighboringList = copy.deepcopy(graph[personVertice].adjacentVertices)
    
    # 50% of being chosen the best vertice
    porcente = 5/10
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
    
def startMessage(statusGame, startTime):
    draw_backGround(backGround, screen)
    draw_edges(graph, screen)
    draw_vertices(graph, screen)
    draw_biomes(biome, screen, BiomeType)
    
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