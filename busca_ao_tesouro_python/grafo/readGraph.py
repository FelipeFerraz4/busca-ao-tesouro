from .vertice import verticeGraph

pontos = [(200, 300), (300, 200)]

def graphRead():
    graph = []
    for item in pontos:
        graph.append(verticeGraph(item))
    return graph