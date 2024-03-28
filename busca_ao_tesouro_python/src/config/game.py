import pygame
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

def gameOn(verticeObjective, end):
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