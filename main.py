from graph import Graph

'''g1 = Graph(7)
g1.add_undirected_edge(0,1)
g1.add_undirected_edge(0,3)
g1.add_undirected_edge(1,2)
g1.add_undirected_edge(2,3)
g1.add_undirected_edge(2,4)
g1.add_undirected_edge(2,6)
print("GRAPH 1:", g1.adj_list)'''

g1 = Graph(10)
g1.add_undirected_edge(0,1)
g1.add_undirected_edge(5,3)
g1.add_undirected_edge(4,5)
g1.add_undirected_edge(6,5)
g1.add_undirected_edge(6,2)
g1.add_undirected_edge(6,9)
g1.add_undirected_edge(7,6)
g1.add_undirected_edge(8,7)
g1.add_undirected_edge(8,9)

print("DEGREE_OUT(0):", g1.degree_out(0))
print("DEGREE_OUT(1):", g1.degree_out(1))
print("HIGHEST_DEGREE_OUT:", g1.highest_degree_out())
print("DEGREE_IN(0):", g1.degree_in(0))
print("DEGREE_IN(1):", g1.degree_in(1))
print("DENSITY: ",  round(g1.density(), 2))
print("IS REGULAR", g1.regular())
print("IS COMPLETE?", g1.complete())
BFS = g1.bfs(5)
print("BFS: ", g1.bfs(5))
print("IS CONEXO: ", g1.conexo(BFS))

