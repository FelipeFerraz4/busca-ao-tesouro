from .vertice import verticeGraph
from .info import points


def graphRead():
    graph = []
    for item in points:
        graph.append(verticeGraph(item[0], item[1], item[2]))
    return graph