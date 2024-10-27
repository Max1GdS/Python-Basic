import networkx as nx
import matplotlib.pyplot as plt

# Crear el grafo G
G = nx.Graph()
G.add_nodes_from(['A', 'B', 'C', 'D'])
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])

# Crear un subgrafo H seleccionando algunos vértices y aristas
H = G.subgraph(['A', 'B', 'C'])  # Seleccionamos un subgrafo con los vértices A, B y C

# Dibujar el grafo G
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
pos_G = nx.spring_layout(G)
nx.draw(G, pos_G, with_labels=True, node_size=700, node_color='lightblue')
plt.title("Grafo G")

# Dibujar el subgrafo H
plt.subplot(1, 2, 2)
pos_H = nx.spring_layout(H)
nx.draw(H, pos_H, with_labels=True, node_size=700, node_color='lightgreen')
plt.title("Subgrafo H")

plt.show()
