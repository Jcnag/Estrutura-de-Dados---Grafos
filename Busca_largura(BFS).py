from collections import deque

class GraphMatrix:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1  #se o grafo for direcionado, remova esta linha

    def print_graph(self):
        for row in self.graph:
            print(row)

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as file:
            num_vertices = int(file.readline())
            graph = cls(num_vertices)

            for line in file:
                u, v = map(int, line.strip().split())
                graph.add_edge(u, v)

        return graph

    def bfs(self, s, t):
        if s < 0 or s >= self.num_vertices or t < 0 or t >= self.num_vertices:
            return []

        visited = [False] * self.num_vertices
        parent = [-1] * self.num_vertices
        queue = deque()

        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.popleft()

            if u == t:
                break

            for v in range(self.num_vertices):
                if self.graph[u][v] == 1 and not visited[v]:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u

        path = []
        current = t

        while current != -1:
            path.append(current)
            current = parent[current]

        return path[::-1] if path[-1] == s else []

if __name__ == "__main__":
    matrix_graph = GraphMatrix.load_from_file("graph_matrix.txt")
    matrix_graph.print_graph()

    source = 0  #vértice de origem
    target = 3  #vértice de destino

    bfs_path = matrix_graph.bfs(source, target)

    if bfs_path:
        print(f"Caminho entre {source} e {target} (BFS): {bfs_path}")
    else:
        print(f"Não há caminho entre {source} e {target}.")
