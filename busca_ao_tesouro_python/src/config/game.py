import pygame

from src.graph.search import breadthFirstSearch, depthFirstSearch
from src.config.button import *
from src.graph.read import graphRead
from src.graph.vertice import *
from src.config.screen import *
from .biome import *

screen = createScreen()
backGround = createBackground()

graph = graphRead()
button_start = create_button_start()
button_next = create_button_next()

biome = create_biome()
BiomeType = 0

def gameOn():
    draw_backGround(backGround, screen)
    draw_edges(graph, screen)
    draw_vertices(graph, screen)
    draw_biomes(biome, screen, BiomeType)
    if button_start.draw(screen):
        print('start')
        print(breadthFirstSearch(graph, graph[10], graph[3]))
    if button_next.draw(screen):
        print('next')
        verticeId = depthFirstSearch(graph, graph[0])
        print(verticeId)