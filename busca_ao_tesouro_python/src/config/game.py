from time import sleep
import pygame
from pygame.locals import *

from src.graph.search import breadthFirstSearch, depthFirstSearch, searchVerticalEmpty
from src.config.button import *
from src.graph.read import graphRead
from src.graph.vertice import *
from src.config.screen import *
from src.graph.informateVertice import draw_informationVetices
from src.config.actionComplement import graph
from .draw_info_vertice import *
from src.character.monster import *
from src.character.weapon import *
from .display import *
from .actionComplement import *

screen = createScreen()
backGround = createBackground()

button_reset = create_button_reset()
button_next = create_button_next()
button_scape = create_button_scape()
button_combat = create_button_combat()
button_get = create_button_get()
button_release = create_button_release()
button_florest = create_button_florest()

pygame.font.init()
fonte = pygame.font.get_default_font()
fontesys = pygame.font.SysFont(fonte, 40)

class Game():
    def __init__(
        self, 
        verticeObjective=3, 
        time=0, 
        startTime=pygame.time.get_ticks(), 
        statusGame=-1, 
        end=False,
        combatMenu=False,
        weaponMenu=False
        ):
      self.verticeObjective = verticeObjective
      self.time = time
      self.startTime = startTime
      self.statusGame = statusGame
      self.end = end
      self.combatMenu = combatMenu
      self.combatRound = 3
      self.weaponMenu = weaponMenu

def gameOn(game, person, monsters, weapons, graph):
    # update_display(game, person, monsters, weapons, graph)
    if game.statusGame == 0:
        displayDefault(game, monsters, person, weapons, graph)
    elif game.statusGame == 3:
        displayEnd(game, monsters, person, weapons, graph)
    elif game.statusGame == 1:
        displayCombat(game, monsters, person, weapons, graph)
    elif game.statusGame == 2:
        displayWeapon(game, monsters, person, weapons, graph)
    else:
        displayStart(game, monsters, weapons, graph)
    message_end(game, person, graph)
    
def message_end(game, person, graph):
    personVertice = depthFirstSearch(graph, graph[0])
    if game.time > 120:
        txttela = fontesys.render('Game Over, tempo esgotado', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        game.statusGame = 3
    if person.health == 0 and person.checkpoints_found == -1:
        txttela = fontesys.render('Game Over, muito danano', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        game.statusGame = 3
    if game.verticeObjective == 10 and personVertice == 10:
        txttela = fontesys.render('Parabéns, fase completa!', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        game.statusGame = 3

