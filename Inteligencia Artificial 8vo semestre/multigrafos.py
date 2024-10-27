import networkx as nx
import matplotlib.pyplot as plt

# Crear un multigrafo
G = nx.MultiGraph()

# Agregar nodos
G.add_nodes_from([1, 2, 3])

# Agregar múltiples aristas entre los mismos nodos
G.add_edge(1, 2)
G.add_edge(2, 3)  
G.add_edge(1, 3)
G.add_edge(3, 2)  # Segunda arista entre los mismos nodos

# Posicionar los nodos usando un layout
pos = nx.spring_layout(G)

# Dibujar los nodos
nx.draw_networkx_nodes(G, pos, node_size=500, node_color="yellow")

# Dibujar las etiquetas de los nodos
nx.draw_networkx_labels(G, pos)

# Dibujar las aristas de forma individual para garantizar la visibilidad
edges = list(G.edges())

# Primera arista entre nodos 1 y 2 (sin curva)
nx.draw_networkx_edges(G, pos, edgelist=[edges[0]], width=2, edge_color='black')

# Segunda arista entre nodos 2 y 3 (con mayor curvatura)
nx.draw_networkx_edges(G, pos, edgelist=[edges[1]], width=2, edge_color='black')

# Primera arista entre nodos 1 y 3 (sin curva)
nx.draw_networkx_edges(G, pos, edgelist=[edges[2]], width=2, edge_color='black')

# Segunda arista entre nodos 2 y 3 (con mayor curvatura)
nx.draw_networkx_edges(G, pos, edgelist=[edges[3]], width=2, edge_color='black', connectionstyle='arc3, rad = 0.4')

# Mostrar el grafo
plt.show()
