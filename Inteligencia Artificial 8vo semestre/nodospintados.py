import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.coloring import greedy_color

# Crear un grafo no dirigido
G = nx.Graph()

# Añadir vértices y aristas al grafo
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Aplicar un algoritmo de coloración de grafos (greedy_color)
color_map = greedy_color(G, strategy="largest_first")

# Crear un diccionario para asignar colores visualmente
color_list = ['red', 'green', 'blue']
node_colors = [color_list[color_map[node]] for node in G.nodes()]

# Dibujar el grafo coloreado
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color=node_colors, edge_color='black')
plt.title("Coloración de un grafo con 3 colores")
plt.show()

# Imprimir los colores asignados a cada nodo
print(f"Colores asignados a cada nodo: {color_map}")
