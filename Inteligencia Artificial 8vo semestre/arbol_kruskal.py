import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo no dirigido y ponderado
G = nx.Graph()

# Definir los vértices y las aristas con pesos
edges = [(1, 2, 4), (1, 3, 1), (2, 3, 2), (2, 4, 5), (3, 4, 3)]

# Agregar las aristas al grafo
G.add_weighted_edges_from(edges)

# Aplicar el algoritmo de Kruskal para encontrar el Árbol de Expansión Mínima
mst = nx.minimum_spanning_tree(G, algorithm="kruskal")

# Mostrar las aristas del árbol de expansión mínima
print("Aristas del Árbol de Expansión Mínima: ", list(mst.edges(data=True)))

# Graficar el grafo original
pos = nx.spring_layout(G)

# Dibujar los nodos
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='yellow')

# Dibujar las aristas del grafo original
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2)

# Dibujar las etiquetas de los nodos
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Dibujar las etiquetas de los pesos de las aristas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Resaltar las aristas del Árbol de Expansión Mínima (MST)
nx.draw_networkx_edges(mst, pos, edgelist=mst.edges(), edge_color='red', width=3)

# Mostrar el grafo
plt.title("Árbol de Expansión Mínima usando Kruskal")
plt.show()