import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir vértices
G.add_nodes_from(["A", "B", "C"])

# Añadir aristas
G.add_edges_from([("A", "B"), ("B","C"), ("C","A")])


# Dibujar el grafo
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)  # Layout para el grafo
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', arrows=True)
plt.title("Grafo Dirigido")
plt.show()



# Calcular el grado de entrada y el grado de salida de cada vértice
grado_entrada = {node: G.in_degree(node) for node in G.nodes()}
grado_salida = {node: G.out_degree(node) for node in G.nodes()}

grado_entrada, grado_salida