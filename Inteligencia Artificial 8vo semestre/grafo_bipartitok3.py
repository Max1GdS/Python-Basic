import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo bipartito K3,3
B = nx.complete_bipartite_graph(3, 3)

# Dibujar el grafo
pos = nx.bipartite_layout(B, nodes=[0, 1, 2])  # Ubicación de los nodos de la primera parte
pos.update(nx.spring_layout(B, pos={3: (0.5, 0), 4: (0.5, 1), 5: (0.5, 2)}, fixed=[3, 4, 5]))

# Dibujar los nodos y las aristas
nx.draw(B, pos, with_labels=True, node_color=['lightblue']*3 + ['lightgreen']*3, node_size=700)
plt.title("Grafo Bipartito K3,3")
plt.show()