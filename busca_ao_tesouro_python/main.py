import pygame
from pygame import mixer
from pygame.locals import *

from src.graph.read import graphRead
from src.config.screen import *

pygame.init()

screen = createScreen()
backGround = createBackground()


run = True

while run:
    draw_backGround(backGround, screen)
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()