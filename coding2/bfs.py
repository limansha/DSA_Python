from collections import deque
from graphs.adj_list_undirected_graph import Graph

class BFS(Graph):
    def __init__(self) -> None:
        super().__init__()
        self.bfs_result = []
        self.visited = set()

    def bfs_traversal(self, start_vertex):
        self.bfs_result = []  # Clear the previous result
        self.visited = set()  # Clear the previous visited set
        self._bfs(start_vertex)

    def _bfs(self, start_vertex):
        queue = deque([start_vertex])
        self.visited.add(start_vertex)

        while queue:
            current_vertex = queue.popleft()
            self.bfs_result.append(current_vertex)

            for neighbor in self.graph[current_vertex]:
                if neighbor not in self.visited:
                    queue.append(neighbor)
                    self.visited.add(neighbor)

    def print_bfs_result(self):
        print("BFS Result:", self.bfs_result)

if __name__ == '__main__':
    g = BFS()

    g.add_node(1, 2)
    g.add_node(1, 3)
    g.add_node(2, 4)
    g.add_node(3, 4)

    print("Graph:")
    print(g)

    start_vertex = 1
    g.bfs_traversal(start_vertex)
    g.print_bfs_result()
