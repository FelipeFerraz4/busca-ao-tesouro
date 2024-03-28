import pygame
from pygame import mixer
from pygame.locals import *

from src.config.game import gameOn

pygame.init()

run = True

#statusGame code 0 - continue, 1 - change goal, 2 - finish game
verticeObjective = 3
end = False
statusGame = -1
startTime = pygame.time.get_ticks()

while run:
    statusGame = gameOn(verticeObjective, end, statusGame, startTime)
    if statusGame == 1:
        verticeObjective = 10
        print('Change Goal')
    if statusGame == 2:
        end = True
    if statusGame == 3:
        verticeObjective = 3
        end = False
        statusGame = -1
        startTime = pygame.time.get_ticks()
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()