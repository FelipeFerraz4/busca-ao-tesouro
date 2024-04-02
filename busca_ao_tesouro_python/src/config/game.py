from time import sleep
import pygame
from pygame.locals import *
import random
import copy

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
    # nextVertice = nextPosition(personVertice, game.verticeObjective, graph)
    if game.time > 120:
        txttela = fontesys.render('Game Over, tempo esgotado', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        game.statusGame = 3
    if person.health == 0 and person.checkpoints_found == -1:
        txttela = fontesys.render('Game Over, muito danano', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        game.statusGame = 3
    if game.verticeObjective == 10 and personVertice == 10:
        # print(personVertice, game.verticeObjective)
        txttela = fontesys.render('Parabéns, fase completa!', 1, (255,255,255))
        screen.blit(txttela, (225, 250))
        game.statusGame = 3

# def update_display(game, person, monsters, weapons, graph):
#     personVertice = depthFirstSearch(graph, graph[0])
#     nextVertice = nextPosition(personVertice, game.verticeObjective, graph)
    
#     if isMonster(monsters, personVertice):
        
    
    # if nextVertice 
    # if game.statusGame > -1:
    #     res = 0
        
    #     personVertice = depthFirstSearch(graph, graph[0])
    #     nextVertice = nextPosition(personVertice, game.verticeObjective)
    #     if isSavePoint(graph, personVertice):
    #         person.checkpoints_found = personVertice
    #         graph[personVertice].savePoint = False
            
    #     if person.health <= 0 and person.checkpoints_found != -1:
    #         resurrect(person, graph, personVertice, weapons)
    #         if person.treasure_percentage >= 0:
    #             game.verticeObjective = 3
    #             person.treasure_percentage = 0
        
    #     if isMonster(monsters, personVertice):
    #         game.combatMenu = True
    #         game.startTime = pygame.time.get_ticks()
            
    #     if isWeapon(weapons, personVertice):
    #         game.weaponMenu = True
        
    #     if game.combatMenu == False and game.weaponMenu == False:
    #         res =  display_default(game, monsters, person, weapons)
    #     elif game.combatMenu == False and game.weaponMenu == True:
    #         res = display_weapon(game, monsters, person, weapons)
    #     else:
    #         res = display_combat(game, monsters, person, weapons)
        
    #     if res != 0:
    #         return res
        
    #     return message_end(game, person, nextVertice)
    # else:
    #     return displayStart(game.statusGame, game.startTime, monsters, weapons)
        

# def display_default(game, monsters, person, weapons):
#     global graph
#     draw_backGround(backGround, screen)
#     draw_edges(graph, screen)
#     draw_vertices(graph, screen)
#     draw_informationVetices(graph, screen, monsters, weapons)
#     person.draw_explorer_info(fontesys, screen, weapons)
#     personVertice = depthFirstSearch(graph, graph[0])
    
#     person.get_treasure(graph, personVertice, weapons)
    
#     if game.end == True:
#         if button_reset.draw(screen):
#             graph = graphRead()
#             sleep(0.1)
#             return 3
#     elif person.weapon != None:
#         if button_release.draw(screen):
#             weapons[person.weapon].vertices = personVertice
#             person.weapon = None
            
#             nextVertice = nextPosition(personVertice, game.verticeObjective)
#             step(personVertice, nextVertice)
#             if nextVertice == 3:
#                 return 1
#             game.time += 1
#             damage_biome(graph, nextVertice, person, weapons)
#             moviment_monster(graph, monsters, weapons)
#             sleep(0.2)
            
#     if button_next.draw(screen) and game.end == False:
#         nextVertice = nextPosition(personVertice, game.verticeObjective)
#         step(personVertice, nextVertice)
#         if personVertice == 3:
#             graph[3].treasure = False
#         if nextVertice == 3:
#             return 1
#         game.time += 1
#         damage_biome(graph, nextVertice, person, weapons)
#         sleep(0.2)
#         moviment_monster(graph, monsters, weapons)
#         print('next')
#     return 0



