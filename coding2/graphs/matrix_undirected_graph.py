#graph as an adjacent list of undirected graph

#as its stored inmatrix we need to have the size of the matrix before hand i.e n or vertex 
#if there is an edge between 0 and 1 node then graph[0][1] and graph[1][0] will be True
class Graph:
    def __init__(self,vertex) -> None:
        self.vertex = vertex
        self.graph = [[False]*vertex for _ in range(vertex)]
    def add_node(self,u,v):
        self.graph[u][v] = True
        self.graph[v][u] = True

#This line converts each element in the current row to a string and joins them with a space in between. The map(str, row) part applies the str function to each element in the row, ensuring that all elements are converted to strings. The join method then concatenates these strings with a space in between.
    def __str__(self):
        #print(self.graph)
        res = ""
        for row in self.graph:
            res += " ".join(map(str,row))+"\n"
        return res


if __name__ == '__main__':
    g = Graph(4) #matrix starts from idex 0
    #g.__init__(5)  we don't call like this as init is like a paramterized constructor
    g.add_node(0,1)
    g.add_node(0,2)
    g.add_node(1,3)
    g.add_node(2,3)
    print(g.__str__())


        
