class Graph:

    def __init__(self):
        self.node = {}
        self.link = {}

    def addNode(self, N):
        self.node[self.Node.id] = N


    def delNode(self, id):
        del self.node[self.Node.id]

    def addLink(self, innode, outnode):
        

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


if __name__ == "__main__":
    pass
