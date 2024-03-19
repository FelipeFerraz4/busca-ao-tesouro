class verticeGraph():
    def __init__(self, id, coordenate, adjacentVertices, person=False, savePoint=False, treasure=False):
        self.id = id
        self.coordinate = (coordenate[0], coordenate[1])
        self.savePoint = savePoint
        self.person = person
        self.adjacentVertices = adjacentVertices
        self.treasure = treasure
        self.item = False
        self.strangeBiome = False
    