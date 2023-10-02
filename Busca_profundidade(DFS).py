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

    def dfs_stack(self, s):
        if s < 0 or s >= self.num_vertices:
            return []

        visited = [False] * self.num_vertices
        stack = [s]
        result = []

        while stack:
            u = stack.pop()

            if not visited[u]:
                result.append(u)
                visited[u] = True

                for v in range(self.num_vertices - 1, -1, -1):
                    if self.graph[u][v] == 1 and not visited[v]:
                        stack.append(v)

        return result

if __name__ == "__main__":
    matrix_graph = GraphMatrix.load_from_file("graph_matrix.txt")
    matrix_graph.print_graph()

    source = 0  #vértice de origem

    dfs_result = matrix_graph.dfs_stack(source)

    print(f"DFS a partir de {source}: {dfs_result}")
