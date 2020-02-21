class Graph:

    def __init__(self):

        self.node = {}
        self.link = []
        self.nodecounter = 0

    class Node:
        def __init__(self, Id, Location, Degrees):
            self.Id = Id
            self.Location = Location
            self.Degrees = Degrees


    class Link:
        def __init__(self, InNodeId, OutNodeId):
            self.InNodeId = InNodeId
            self.OutNodeId = OutNodeId


    def addNode(self, newnode):

        self.node[self.nodecounter] = newnode
        self.nodecounter += 1

    def delNode(self, Id):
        if self.node[Id]:
            del self.node[Id]
        else:
            print('this node is not exist for deleting')


    def addLink(self, Link):
        innode = Link.InNodeId
        outnode = Link.OutNodeId
        self.link.append((innode, outnode))


    def delLink(self, innode, outnode):
        if self.link.count((innode, outnode)) >= 1:
            self.link.remove((innode, outnode))
        else:
            print('there is no such link to remove!!!')

    def ShowOutPut(self):

        print(self.node)
        print(self.link)


if __name__ == "__main__":
    G = Graph()
    G.addNode(G.Node(0, 13, 4))
    G.addNode(G.Node(1, 18, 3))
    G.addNode(G.Node(2, 13, 4))
    G.addNode(G.Node(3, 18, 3))
    G.addLink(G.Link(0, 1))
    G.addLink(G.Link(1, 3))
    G.addLink(G.Link(2, 1))
    G.delNode(1)
    G.delLink(3, 1)
    G.ShowOutPut()




