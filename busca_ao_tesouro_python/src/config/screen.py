import pygame

from src.graph.search import breadthFirstSearch, depthFirstSearch
from src.config.button import *
from src.graph.read import graphRead
from src.graph.vertice import *
from .biome import *

screen_width = 1000
screen_height = 600

graph = graphRead()
button_start = create_button_start()
button_next = create_button_next()

biome = create_biome()
BiomeType = 0

def createScreen():
    screen = pygame.display.set_mode((screen_width, screen_height), 0)
    pygame.display.set_caption('Busca ao Tesouro')
    backGround = pygame.image.load('./src/assets/mapa_image/image.png')
    backGround = pygame.transform.scale(backGround, (screen_width - 200, screen_height))
    return screen

def createBackground():
    backGround = pygame.image.load('./src/assets/mapa_image/image.png')
    backGround = pygame.transform.scale(backGround, (screen_width - 200, screen_height))
    return backGround

def draw_backGround(backGround, surface):
    surface.blit(backGround, (0, 0))
    draw_edges(graph, surface)
    draw_vertices(graph, surface)
    draw_biomes(biome, surface, BiomeType)
    if button_start.draw(surface):
        print('start')
        print(breadthFirstSearch(graph, graph[10], graph[3]))
    if button_next.draw(surface):
        print('next')
        verticeId = depthFirstSearch(graph, graph[0])
        print(verticeId)