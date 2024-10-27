import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo no dirigido
G = nx.Graph()

# Agregar vértices y aristas al grafo
G.add_nodes_from(['A', 'B', 'C'])
aristas=G.add_edges_from([("A", "B"), ("B","C"), ("C","A")])

# Posicionar los nodos usando un layout
pos = nx.spring_layout(G)

# Dibujar los nodos
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='yellow')

# Dibujar las aristas
nx.draw_networkx_edges(G, pos, edgelist=aristas, width=2)

# Dibujar las etiquetas de los nodos
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Mostrar el grafo
plt.title("Grafo con vértices V={A,B,C,D} y aristas E={(A,B),(B,C),(C,D)}")
plt.show()