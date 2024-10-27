import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo no dirigido
G = nx.Graph()

# Agregar nodos
G.add_nodes_from([1, 2, 3, 4])

# Agregar aristas con pesos
# El formato es: (nodo1, nodo2, {'weight': peso})
G.add_edges_from([(1, 2, {'weight': 6}),
                  (2, 3, {'weight': 1}),
                  (3, 4, {'weight': 3}),
                  (4, 1, {'weight': 3}),
                  (2, 4, {'weight': 5})])

# Mostrar nodos y aristas
print("Nodos del grafo: ", G.nodes())
print("Aristas del grafo con pesos: ", G.edges(data=True))

# Mostrar los vecinos del nodo 1
print("Los vecinos de 1 en G son ", list(G.adj[1]))

# Mostrar los vecinos del nodo 4
print("Los vecinos de 4 en G son ", list(G.adj[4]))

# Asignar el nodo inicial y el nodo de destino para la búsqueda
source = 1
target = 3

# Encontrar el camino más corto basado en los pesos de las aristas
shortest_path = nx.shortest_path(G, source=source, target=target, weight='weight')

# Imprimir el camino más corto y su longitud
shortest_path_length = nx.shortest_path_length(G, source=source, target=target, weight='weight')
print(f"El camino más corto entre {source} y {target}: {shortest_path} con una longitud total de {shortest_path_length}")

# Graficar el grafo
pos = nx.spring_layout(G)  # Posiciones para todos los nodos

# Dibujar los nodos
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='yellow')

# Dibujar las aristas
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=2)

# Dibujar las etiquetas de los nodos
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Dibujar las etiquetas de los pesos de las aristas
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Mostrar el grafo
plt.title("Grafo con pesos en las aristas")
plt.show()