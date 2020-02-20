class Graph:

    def __init__(self):

        self.node = {}
        self.link = []
        self.nodecounter = 0

    def addNode(self, newnode):

        self.node[self.nodecounter] = newnode
        self.nodecounter += 1

    def delNode(self, Id):

        del self.node[self.nodecounter]

    def addLink(self, innode, outnode):

        self.link.append((innode, outnode))


    def delLink(self, innode, outnode):
        
        self.link.remove((innode, outnode))


class Node:
    def __init__(self, Id, Location, Degrees):
        self.Id = Id
        self.Location = Location
        self.Degrees = Degrees

class Link:
    def __init__(self, InNodeId, OutNodeId):
        self.InNodeId = InNodeId
        self.OutNodeId = OutNodeId


if __name__ == "__main__":
    G = Graph
    G.addNode(Node(0, 13, 4))
    G.addNode(Node(1, 18, 3))
    G.addLink(Link(0, 1))



