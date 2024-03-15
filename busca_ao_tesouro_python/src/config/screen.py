import pygame

screen_width = 1000
screen_height = 600
colorPoint = (50, 100, 200)

def createScreen():
    screen = pygame.display.set_mode((screen_width, screen_height), 0)
    pygame.display.set_caption('Busca ao Tesouro')
    backGround = pygame.image.load('./src/assets/mapa_image/image.png')
    backGround = pygame.transform.scale(backGround, (screen_width - 200, screen_height))
    return screen

def createBackground():
    backGround = pygame.image.load('./src/assets/mapa_image/image.png')
    backGround = pygame.transform.scale(backGround, (screen_width - 200, screen_height))
    return backGround

def draw_graph(graph, screen):
    for vertice in graph:
        # print(vertice.adjacentVertices)
        pygame.draw.circle(screen, colorPoint, vertice.coordinate, 5, 0)
        for neighboring in vertice.adjacentVertices:
            pygame.draw.line(screen, colorPoint, vertice.coordinate, graph[neighboring].coordinate, 2)

def draw_backGround(graph, backGround, screen):
    screen.blit(backGround, (0, 0))
    draw_graph(graph, screen)
