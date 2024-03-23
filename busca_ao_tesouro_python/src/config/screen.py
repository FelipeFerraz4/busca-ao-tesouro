import pygame

from src.graph.search import breadthFirstSearch, depthFirstSearch
from src.config.button import *
from src.graph.read import graphRead
from src.graph.vertice import *
from .biome import *

screen_width = 1000
screen_height = 600

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
