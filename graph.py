class Graph:
    def __init__(self, node_count: int, edge_count: int = 0, adj_list: list[list[int]] = []) -> None:
        self.node_count = node_count
        self.edge_count = edge_count
        self.adj_list = adj_list
        if adj_list == []:
            for _ in range(self.node_count):
                self.adj_list.append([])

    def add_directed_edge(self, u: int, v: int):
        if u < 0 or u >= len(self.adj_list) or v < 0 or v >= len(self.adj_list):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.node_count - 1})")
        self.adj_list[u].append(v)
        self.edge_count += 1

    def add_undirected_edge(self, u: int, v: int):
        self.add_directed_edge(u, v)
        self.add_directed_edge(v, u)

    def degree_out(self, u: int) -> int:
        return len(self.adj_list[u])

    def degree_in(self, u: int) -> int:
        degree = 0
        for i in range(len(self.adj_list)):
            if u in self.adj_list[i]:
                degree += 1
        return degree

    def highest_degree_out(self) -> int:
        max_degree_out = 0
        highest_degree_node = 0
        for i in range(self.node_count):
            degree_out_node_i = self.degree_out(i)
            if max_degree_out < degree_out_node_i:
                max_degree_out = degree_out_node_i
                highest_degree_node = i
        return highest_degree_node

    def highest_degree_in(self) -> int:
        max_degree_in = float("inf")
        highest_degree_node = 0
        for i in range(self.node_count):
            degree_in_node_i = self.degree_in(i)
            if max_degree_in < degree_in_node_i:
                max_degree_in = degree_in_node_i
                highest_degree_node = i
        return highest_degree_node
    
    def density(self):
        ''' Calculates the density of the graph: 
            D = [E] / ([V] * ([V] - 1))'''
        density = self.edge_count / (self.node_count * (self.node_count -1))
        return density

    def complete(self): 
        '''[E] tem V-1 elementos'''

        for i in range(len(self.adj_list)):
            if(len(self.adj_list[i]) != self.node_count-1):
                return False
            return True

        '''Melhores maneiras:'''
        #return self.density()==1
        #return self.edge_count == self.node_count * (self.node_count-1)
        
    def regular(self):
        '''Todos [E] são iguais'''
        tamanho = len(self.adj_list[0])
        for i in range(len(self.adj_list)):
            if(len(self.adj_list[i]) != tamanho):
                return False
        return True
    
    def complement(self):
        # Inicializa o grafo complemento
        complement = [[0 for i in range(len(self.adj_list)-1)] for j in range(len(self.adj_list)-1)]
        # Para cada vértice do grafo original
        for i in range(len(self.adj_list)-1):
            # Para cada vértice não adjacente ao vértice atual
            for j in range(len(self.adj_list)-1):
                if i != j and self.adj_list[i] == 0:
                    # Adiciona uma aresta no complemento
                    complement[i][j] = 1
        return complement

    def subgraph(self, g2):
        pass

    def _str_(self):
        repr = ""
        for adj in self.adj_list:
            repr += str(adj) + "\n"
        return repr