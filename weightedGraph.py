class WeightedGraph:
    def __init__(self, node_count: int = 0, edge_count: int = 0, adj_list: list[list[tuple[int, int]]] = []) -> None:
        self.node_count = node_count
        self.edge_count = edge_count
        self.adj_list = adj_list
        if adj_list == []:
            for _ in range(self.node_count):
                self.adj_list.append([])
    
    
    def add_directed_edge(self, u: int, v: int, w:int):
        if u < 0 or u >= len(self.adj_list) or v < 0 or v >= len(self.adj_list):
            print(f"Node u={u} or v={v} is out of allowed range (0, {self.node_count - 1})")
        self.adj_list[u].append((v, w))
        self.edge_count +=1

    def add_undirected_edge(self, u: int, v: int, w:int):
        self.add_directed_edge(u, v, w)
        self.add_directed_edge(v, u, w)
    
    def read_file(self, file_name):
        """Read graph file in Dimacs format"""
        with open(file_name, "r") as file:
            i = 0
            for line in file:
                i += 1
                if i == 1:
                    header = line.split(" ")
                    self.node_count = int(header[0])
                    self.adj_list = [[] for i in range(self.node_count)]
                else:
                    edge_data = line.split(" ")
                    u = int(edge_data[0])  # Source node
                    v = int(edge_data[1])  # Sink node
                    w = int(edge_data[2])  # Edge (u, v) weight
                    self.add_directed_edge(u, v, w)

    def bellman_ford(self, s):
        dist = []
        pred = []
        for v in range(self.node_count):
            dist[v] = float("inf")
            pred[v] = None
        
        dist[s]=0

        for _ in range(self.node_count - 1):
            for u, v, w in self.edge_count():
                if dist[v] > dist[u]+w:
                    dist[v] = dist[u]+w
                    pred[v] = u


