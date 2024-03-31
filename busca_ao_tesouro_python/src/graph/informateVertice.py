from src.graph.search import depthFirstSearch
from src.config.draw_info_vertice import *

def draw_informationVetices(graph, surface, monster):
    personVertice = depthFirstSearch(graph, graph[0])
    monsters = -1
    for item in monster:
        if item.vertices == personVertice:
            monsters = item.index
    biomeType = graph[personVertice].strangeBiome
    if monsters != -1 and monster[monsters].type == 'hawk':
        info = create_monster_hawk()
    elif monsters != -1 and monster[monsters].type == 'ant':
        info = create_monster_ant()
    elif monsters != -1 and monster[monsters].type == 'jaguar':
        info = create_monster_jaguar()
    elif monsters != -1 and monster[monsters].type == 'alligator':
        info = create_monster_alligator()
    elif biomeType == 0:
        info = create_biome_0()
    elif biomeType == 1:
        info = create_biome_1()
    elif biomeType == 2:
        info = create_biome_2()
    elif biomeType == 3:
        info = create_biome_3()
    elif biomeType == 4:
        info = create_biome_4()
    elif biomeType == 5:
        info = create_biome_5()
    elif biomeType == -1 and graph[personVertice].treasure:
        info = create_biome_treasure()  
    else:
        info = create_biome()
        
    surface.blit(info.image, (info.rect.x, info.rect.y))