import pygame
from pygame import mixer
from pygame.locals import *

from src.config.game import gameOn

pygame.init()

run = True

while run:
    gameOn()
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()