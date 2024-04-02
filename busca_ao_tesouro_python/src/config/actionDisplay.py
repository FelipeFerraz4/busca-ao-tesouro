from src.graph.search import depthFirstSearch, searchVerticalEmpty
from src.config.actionComplement import *
from src.graph.vertice import *
from src.character.monster import isMonster
from time import sleep
from src.character.weaponRead import weaponsRead
from src.graph.read import graphRead
# from .actionComplement import *

def reset(game, graph, monsters, person, weapons):
    game.time = 0
    game.verticeObjective = 3
    game.statusGame = -1
    person.health = 100
    person.treasure_percentage = 0
    person.weapon = None
    game.end = True
    
def combat(game, graph, monsters, person, weapons):
    personVertice = depthFirstSearch(graph, graph[0])
    monster = monsters[getMonster(monsters, personVertice)]
    #dano do monstro na rodada
    person.take_damage(monster.attack_points, weapons)
    
    #atualiza a porcetagem do tesouro
    update_treasure(person, weapons)
    
    #dano do personagem na rodada
    if person.weapon == None:
        monster.take_damage(person.attack)
    else:
        monster.take_damage(person.attack + weapons[person.weapon].attack_bonus)
    
    #verifico se o monstro morreu
    if monster.health_points == 0:
        monster.health_points = 100
        monster.vertices = searchVerticalEmpty(graph, graph[random.randint(0, len(graph))], weapons)
        game.combatMenu = False
        game.combatRound = 3
    
    if game.combatRound == 1:
        #   muda display
        game.statusGame = 0
        #   Restaur o combate
        game.combatRound = 3
        #   Faz o vertice passar
        next(game, graph, monsters, person, weapons)
    else:
        game.combatRound -= 1
        
def scape(game, graph, monsters, person, weapons):
    personVertice = depthFirstSearch(graph, graph[0])
    monster = monsters[getMonster(monsters, personVertice)]
    # game.time += 1
    #   Faz o vertice passar
    game.statusGame = 0
    
    # dano da fuga
    person.take_damage(monster.attack_points, weapons)
    
    #atualiza a porcetagem do tesouro
    update_treasure(person, weapons)
    
    #restaurando o combate
    game.combatRound = 3
    next(game, graph, monsters, person, weapons)
    
def next(game, graph, monsters, person, weapons):
    game.time += 1
    personVertice = depthFirstSearch(graph, graph[0])
    nextVertice = nextPosition(personVertice, game.verticeObjective, graph)

    #change the person's vertice
    graph[personVertice].person = False
    graph[nextVertice].person = True
    
    #pegar tesouro
    if personVertice == 3:
        graph[3].treasure = False

    # movimentação dos monstro
    moviment_monster(graph, monsters, weapons)
    
    # dano do bioma
    damage_biome(graph, nextVertice, person, weapons)
    
    if isMonster(monsters, nextVertice):
        game.statusGame = 1
        
    if isWeapon(weapons, nextVertice):
        game.statusGame = 2
        
    
def get_weapon(game, graph, monsters, person, weapons):
    personVertice = depthFirstSearch(graph, graph[0])
    
    #pegar a arma
    weapon = getWeapon(weapons, personVertice)
    
    #indexando o vertice a arma
    if person.weapon != None:
        weapons[weapon].vertices = personVertice
        
    #indexando a arma a pessoa
    person.weapon = weapon
    
    print(person.weapon)
    #retirando a arma do vertice
    weapons[weapon].vertices = -1
    
    #atualizando o tesouro
    update_treasure(person, weapons)
    
    sleep(0.3)
    game.time += 1
    game.statusGame = 0
    next(game, graph, monsters, person, weapons)
    
def release(game, graph, monsters, person, weapons):
    personVertice = depthFirstSearch(graph, graph[0])
    
    #deixando a arma no vertice
    weapons[person.weapon].vertices = personVertice
    
    #retirar a arma do personagem
    person.weapon = None
    
    
    game.statusGame = 0
    next(game, graph, monsters, person, weapons)
    
    
    