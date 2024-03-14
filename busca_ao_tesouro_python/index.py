import pygame
from pygame import mixer
from pygame.locals import *

from grafo.readGraph import graphRead

pygame.init()

screen_width = 1000
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), 0)
colorPoint = (50, 100, 200)

pygame.display.set_caption('Busca ao Tesouro')
run = True

backGround = pygame.image.load('./assets/mapa_image/image.png')
backGround = pygame.transform.scale(backGround, (screen_width - 200, screen_height))

Grafo = [(180, 290), (300, 200), (200, 200), (450, 100), (450, 150), 
         (400, 150), (500, 150), (360, 180), (420, 190), (360, 300),
         (340, 480), (300, 430), (370, 450), (350, 410), (280, 380),
         (400, 350), (450, 400), (430, 450), (480, 470), (520, 420),
         (230, 260), (270, 285), (315, 325), (340, 260), (422, 255),
         (472, 295), (502, 360), (532, 310), (605, 340), (605, 260),
         (510, 250), (530, 195), (245, 325), (435, 325), (465, 225)
         ]

def draw_vertices(Grafo):
    for vertice in Grafo:
        pygame.draw.circle(screen, colorPoint, vertice, 5, 0)
def draw_backGround(Grafo):
    screen.blit(backGround, (0, 0))
    draw_vertices(Grafo)

while run:
    draw_backGround(Grafo)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()