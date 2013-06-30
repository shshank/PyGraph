class Graph:
    def __init__(self,name=""):
        self.name = name
        self.list_neighbor = {}
        self.list_node = {}
    def add_node(self,node):
        self.list_node[node] = True

    def add_edge(self,node,nodebis):
        try :
            self.list_neighbor[node].append(nodebis)
        except :
            self.list_neighbor[node] = []
            self.list_neighbor[node].append(nodebis)
        try :
            self.list_neighbor[nodebis].append(node)
        except :
            self.list_neighbor[nodebis] = []
            self.list_neighbor[nodebis].append(node)
    def neighbors(self,node):
        try :
            return self.list_neighbor[node]
        except :
            return []
    def nodes(self):
        return self.list_node.keys()
    def delete_edge(self,node,nodebis):
        self.list_neighbor[node].remove(nodebis)
        self.list_neighbor[nodebis].remove(node)
    def delete_node(self,node):
        del self.list_node[node]
        try :
            for nodebis in self.list_neighbor[node] :
                self.list_neighbor[nodebis].remove(node)
            del self.list_neighbor[node]
        except :
            return "error"

def degree(Graph, node):
    return len(Graph.neighbors(node))

def max_degree(Graph):
    max_degree = 0
    for key in Graph.list_neighbor:
        if max_degree<len(Graph.list_neighbor[key]):
            max_degree = len(Graph.list_neighbor[key])
    return max_degree



if __name__ == "__main__":

    #testing api
    G = Graph("test")
    G.add_node(1)
    G.add_node(2)
    G.add_node(4)
    G.add_node(5)
    G.add_node(8)
    G.add_edge(1,2)
    G.add_edge(2,4)
    G.add_edge(4,5)
    print G.nodes
    print "The nodes in the Graph %s are: \n %s" %(G.name, G.list_node)
    print "The adjacency list is : \n"
    for node in G.list_node:
        neighbors = G.neighbors(node)
        print "%s is connected to %s" %(node, neighbors)