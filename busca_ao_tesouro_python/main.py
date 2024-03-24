import pygame
from pygame import mixer
from pygame.locals import *

from src.config.game import gameOn

pygame.init()

run = True

#status code 0 - continue, 1 - change goal, 2 - finish game
verticeObjective = 3
end = False

while run:
    status = gameOn(verticeObjective, end)
    if status == 1:
        verticeObjective = 10
        print('Change Goal')
    if status == 2:
        print('Game Over')
        end = True
        # run = False
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()