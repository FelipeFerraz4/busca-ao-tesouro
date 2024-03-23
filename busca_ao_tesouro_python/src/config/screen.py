import pygame

from src.graph.search import breadthFirstSearch, depthFirstSearch
from src.config.button import *
from src.graph.read import graphRead
from .biome import *

screen_width = 1000
screen_height = 600

colorPointBlue = (50, 100, 200) #azul
colorPointRed = (200, 50, 100) #vermelho
colorPointGreen = (50, 200, 100) #verde
colorPointWhite = (255, 255, 255) #branco

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

def draw_edges(graph, surface):
    for vertice in graph:
        for neighboring in vertice.adjacentVertices:
            pygame.draw.line(surface, colorPointBlue, vertice.coordinate, graph[neighboring].coordinate, 2)

def draw_vertices(graph, surface):
    for vertice in graph:
        if vertice.person == True:
            pygame.draw.circle(surface, colorPointGreen, vertice.coordinate, 8, 0)
        elif vertice.savePoint == True:
            pygame.draw.circle(surface, colorPointWhite, vertice.coordinate, 8, 0)
        elif vertice.treasure == True:
            pygame.draw.circle(surface, colorPointRed, vertice.coordinate, 8, 0)
        else:
            pygame.draw.circle(surface, colorPointBlue, vertice.coordinate, 8, 0)

def draw_biomes(graph, surface, type):
    biome.draw_biome(surface)

def draw_backGround(backGround, surface):
    surface.blit(backGround, (0, 0))
    draw_edges(graph, surface)
    draw_vertices(graph, surface)
    draw_biomes(graph, surface, BiomeType)
    if button_start.draw(surface):
        print('start')
        print(breadthFirstSearch(graph, graph[10], graph[3]))
    if button_next.draw(surface):
        print('next')
        verticeId = depthFirstSearch(graph, graph[0])
        print(verticeId)