import pygame
from pygame import mixer
from pygame.locals import *

from src.config.game import Game, gameOn

pygame.init()

run = True

#statusGame code 0 - continue, 1 - change goal, 2 - finish game, 3 - reset 
game = Game()
# verticeObjective = 3
# end = False
# statusGame = -1
# startTime = pygame.time.get_ticks()

while run:
    game.statusGame = gameOn(game)
    print(game.time)
    if game.statusGame == 1:
        game.verticeObjective = 10
        print('Change Goal')
    if game.statusGame == 2:
        game.end = True
    if game.statusGame == 3:
        game.verticeObjective = 3
        game.end = False
        game.statusGame = -1
        game.startTime = pygame.time.get_ticks()
        game.time = 0
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()