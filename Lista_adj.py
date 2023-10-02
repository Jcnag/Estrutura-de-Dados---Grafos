class GraphAdjList: #Grafo com Lista de Adjacência
    def __init__(self, num_vertices): #inicia uma lista vazia para cada vértice
        self.num_vertices = num_vertices
        self.graph = [[] for _ in range(num_vertices)]

    def add_edge(self, u, v): #adiciona uma aresta entre os vértices u e v, inserindo v na lista de adjacência de u e vice-versa 
        self.graph[u].append(v)
        self.graph[v].append(u)  #se o grafo for direcionado, remova esta linha

    def print_graph(self): #impressão da lista
        for i, adjacents in enumerate(self.graph):
            print(f"Vertex {i}: {adjacents}")
