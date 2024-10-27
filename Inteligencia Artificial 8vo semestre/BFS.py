import networkx as nx
from collections import deque
import matplotlib.pyplot as plt

# Crear un grafo no dirigido
G = nx.Graph()

# Definir los vértices
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Definir las aristas (conexiones entre los vértices)
edges = [('A', 'B'), ('B', 'D'), ('C', 'E'), 
         ('D', 'F'), ('E', 'F'), ('F', 'G')]

# Agregar vértices y aristas al grafo
G.add_nodes_from(vertices)
G.add_edges_from(edges)

# Implementación del algoritmo BFS para encontrar el camino más corto
def bfs_shortest_path(graph, start, goal):
    # Cola para realizar la búsqueda por anchura
    queue = deque([[start]])
    # Conjunto para registrar los nodos visitados
    visited = set()
    
    while queue:
        # Extraemos el primer camino de la cola
        path = queue.popleft()
        # Tomamos el último nodo del camino actual
        node = path[-1]
        
        # Si encontramos el nodo objetivo, retornamos el camino
        if node == goal:
            return path
        
        # Si el nodo no ha sido visitado
        elif node not in visited:
            # Marcamos el nodo como visitado
            visited.add(node)
            # Recorremos los vecinos del nodo
            for neighbor in graph.neighbors(node):
                # Creamos un nuevo camino que incluye al vecino
                new_path = list(path)
                new_path.append(neighbor)
                # Agregamos el nuevo camino a la cola
                queue.append(new_path)
    
    # Si no encontramos un camino
    return None

# Ejemplo: Encontrar el camino más corto entre 'A' y 'G'
start_node = 'A'
goal_node = 'G'
shortest_path = bfs_shortest_path(G, start_node, goal_node)

# Imprimir el resultado
print(f"El camino más corto entre {start_node} y {goal_node} es: {shortest_path}")

#graficalo
# Posicionar los nodos usando un layout
pos = nx.spring_layout(G)

# Dibujar los nodos

nx.draw_networkx_nodes(G, pos, node_size=700, node_color='yellow')

# Dibujar las aristas
nx.draw_networkx_edges(G, pos, edgelist=edges, width=2)

# Dibujar las etiquetas de los nodos
nx.draw_networkx_labels(G, pos, font_size=12, font_family='sans-serif')

# Dibujar el camino más corto
shortest_edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
nx.draw_networkx_edges(G, pos, edgelist=shortest_edges, edge_color='red', width=2)

# Mostrar el grafo
plt.title("Grafo con vértices V={A,B,C,D,E,F,G} y aristas E={(A,B), (A,C), (B,D), (C,E), (D,F), (E,F), (F,G)}")

plt.show()
# Compare this snippet from Inteligencia%20Artificial%208vo%20semestre/BFS.py:
