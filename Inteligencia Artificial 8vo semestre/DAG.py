import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido (DAG)
G = nx.DiGraph()

# Añadir vértices (nodos) que representan tareas
G.add_nodes_from([1, 2, 3, 4, 5])

# Añadir aristas que representan dependencias entre tareas
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

# Dibujar el grafo
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Layout para el grafo
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', arrows=True)
plt.title("Grafo Acíclico Dirigido (DAG)")
plt.show()

# Realizar la ordenación topológica
topological_order = list(nx.topological_sort(G))

# Imprimir el orden topológico
print(f"Ordenación Topológica: {topological_order}")
