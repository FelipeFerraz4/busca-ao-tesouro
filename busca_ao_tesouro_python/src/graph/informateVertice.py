from src.graph.search import depthFirstSearch
from src.config.biome import *

def draw_informationVetices(graph, surface):
    personVertice = depthFirstSearch(graph, graph[0])
    biomeType = graph[personVertice].strangeBiome
    if biomeType == 0:
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
    else:
        info = create_biome()
        
    surface.blit(info.image, (info.rect.x, info.rect.y))