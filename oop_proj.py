class Graph:
    
    def __init__(self):
        self.Node = {}
        self.Link = {}

    def addNode(self, node):
        pass

    def delNode(self):
        pass

    def addLink(self):
        pass

    def delLink(self):
        pass



class Node(Graph):
    def __init__(self, id, Location, Degrees):
        self.id = id
        self.Location = Location
        self.Degrees = Degrees

class Link(Graph) :
    def __init__(self, InNodeId, OutNodeId):
        self.InNodeId = InNodeId
        self.OutNodeId = OutNodeId

    