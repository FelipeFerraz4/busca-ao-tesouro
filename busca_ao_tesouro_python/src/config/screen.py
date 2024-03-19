import pygame

from src.graph.search import breadthFirstSearch
from .button import Button

screen_width = 1000
screen_height = 600
colorPointBlue = (50, 100, 200) #azul
colorPointRed = (200, 50, 100) #vermelho
colorPointGreen = (50, 200, 100) #verde
colorPointWhite = (255, 255, 255) #branco

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

def draw_backGround(graph, backGround, surface, button_start):
    surface.blit(backGround, (0, 0))
    draw_edges(graph, surface)
    draw_vertices(graph, surface)
    if button_start.draw(surface):
        print('start')
        print(breadthFirstSearch(graph, graph[10], graph[3]))
    