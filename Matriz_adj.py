class GraphMatrix: #classe de Grafo com Matriz de Adjacência
    def __init__(self, num_vertices): #criação de adjacência inicialmente preenchida com zeros
        self.num_vertices = num_vertices
        self.graph = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v): #add aresta entre os vértices u e v
        self.graph[u][v] = 1
        self.graph[v][u] = 1  #se o grafo for direcionado, remover esta linha

    def print_graph(self): #impressão da matriz
        for row in self.graph:
            print(row)
