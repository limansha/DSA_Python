#graph as an adjacent list of directed graph

class Graph:
    def __init__(self) -> None:
        self.graph = {} #dict

    def add_node(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v) # we will have directed edge from u -> v 
        
    def __str__(self) -> str:
        res = ""
        for vertex,edges in self.graph.items():
            res +=f"vertex {vertex} edges {edges}\n"
        return res
 
if __name__ == '__main__':
    g = Graph()
    g.add_node(1,2)
    g.add_node(1,3)
    g.add_node(2,4)
    g.add_node(3,4)

    print(g.__str__())
