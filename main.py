from graph import Graph
from weightedGraph import WeightedGraph

g2 = WeightedGraph(5)
#g2.add_directed_edge(0, 1, 6)
#g2.add_directed_edge(0, 2, 2)
#g2.add_directed_edge(1, 2, 3)
#g2.add_directed_edge(1, 3, 1)
#g2.add_directed_edge(1, 4, 3)
#g2.add_directed_edge(2, 1, 2)
#g2.add_directed_edge(2, 3, 5)
#g2.add_directed_edge(3, 4, 3)
g2.read_file("toy.txt")
print(g2.adj_list)
print(g2.bellman_ford(0))

'''
# BFS AND CONNECTED (LESSON 3)
g1 = Graph(10, adj_list=[])
g1.add_undirected_edge(0, 1)
g1.add_undirected_edge(2, 3)
g1.add_undirected_edge(3, 5)
g1.add_undirected_edge(5, 4)
g1.add_undirected_edge(5, 6)
g1.add_undirected_edge(6, 7)
g1.add_undirected_edge(6, 9)
g1.add_undirected_edge(7, 8)
g1.add_undirected_edge(8, 9)
print("G1: ", g1.adj_list)  
print("GRAPH 1:", g1.adj_list)
print("DEGREE_OUT(0):", g1.degree_out(0))
print("DEGREE_OUT(1):", g1.degree_out(1))
print("HIGHEST_DEGREE_OUT:", g1.highest_degree_out())
print("DEGREE_IN(0):", g1.degree_in(0))
print("DEGREE_IN(1):", g1.degree_in(1))
print("DENSITY:", g1.density())
print("COMPLETE:", g1.complete())
print("REGULAR:", g1.regular())

#print("COMPLEMENT OF G1: ", g1.complement())

g2 = Graph(2, adj_list=[])
g2.add_undirected_edge(0, 1)
print("G2 IS SUBGRAPH OF G1?", g1.subgraph(g2))  # True

print("BFS FROM 5:", g1.bfs(5))  # [5, 3, 4, 6, 2, 7, 9, 8]
print("DFS FROM 5:", g1.dfs(5))  # [5, 3, 2, 4, 6, 7, 8, 9]
print("CONNECTED (conexo): ", g1.connected())
print("NEIGHBOOR: ", g1.is_neighbor(1, 2))  # False
print("NEIGHBOOR: ", g1.is_neighbor(2, 3))  # True
print("MATRIZ: ", g1.to_adj_matrix())
print("VALID WALK: ", g1.is_valid_walk([2, 3, 5, 4]))  # True
print("VALID WALK: ", g1.is_valid_walk([0, 1, 2, 1]))  # False (there is no edge from 2 to 1)
print("VALID PATH: ", g1.is_valid_path([2, 3, 5, 6, 7, 8, 9]))  # True
print("VALID PATH: ", g1.is_valid_path([5, 6, 7, 9]))  # false
print("CLOSED: ", g1.is_closed([6, 7, 8, 9, 6]))  # True
print("CLOSED: ", g1.is_closed([2, 3, 5, 4]))  # False


# EXERCISES
print(g1.is_closed([0, 2, 3, 0]))  # True
print(g1.is_closed([0, 2, 3]))  # False
print(g1.degree_in_more_than(1))  # [0, 2]
print(g1.degree_out_more_than(1))  # [0, 2]
print(g1.nodes_having_in_degree(1))  # [1, 3]
print(g1.nodes_having_out_degree(1))  # [1, 3]
print(g1.diff_min_max_in_degree())  # 1
print(g1.diff_min_max_out_degree())  # 1
print(g1.is_directed())  # False
g1.remove_directed_edge(0, 1)
print(g1.adj_list)  # [[2], [0], [0, 3], [2]]
print(g1.is_directed())  # True
g1.remove_undirected_edge(2, 3)
print(g1.adj_list)  # [[2], [0], [0], []]
g1.add_node()
print(g1.adj_list)  # [[2], [0], [0], [], []] (the graph now has 5 nodes)
g1.add_undirected_edge(2, 4)
print(g1.adj_list)  # [[2], [0], [0, 4], [], [2]]
g1.remove_node(0)
print(g1.adj_list)  # [[], [3], [], [1]] (node 1 becomes 0, node 2 becomes 1, 3 becomes 2, and 4 becomes 3)
'''