import pygame
from pygame import mixer
from pygame.locals import *
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height), 0)

pygame.display.set_caption('Busca ao Tesouro')
run = True

backGround = pygame.image.load('./assets/mapa_image/image.png')
backGround = pygame.transform.scale(backGround, (screen_width, screen_height))

def draw_backGround():
    screen.blit(backGround, (0, 0))

while run:
    draw_backGround()
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()