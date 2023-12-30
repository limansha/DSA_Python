from graphs.adj_list_undirected_graph import Graph

class DFS(Graph):
    def __init__(self) -> None:
        super().__init__() #inherited
        self.dfs_result = []
        self.visited = set()

    def dfs_traversal(self, start_vertex):
        self.dfs_result = []  # Clear the previous result
        self.visited = set()  # Clear the previous visited set
        self._dfs(start_vertex)

    def _dfs(self, vertex):
        self.visited.add(vertex)
        self.dfs_result.append(vertex)

        for neighbor in self.graph[vertex]:
            if neighbor not in self.visited:
                self._dfs(neighbor)

    def print_dfs_result(self):
        print("DFS Result:", self.dfs_result)

if __name__ == '__main__':
    g = DFS()

    g.add_node(1, 2)
    g.add_node(1, 3)
    g.add_node(2, 4)
    g.add_node(3, 4)

    print("Graph:")
    print(g)

    start_vertex = 1
    g.dfs_traversal(start_vertex)
    g.print_dfs_result()

