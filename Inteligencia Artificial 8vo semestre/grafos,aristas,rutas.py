import networkx as nx
import matplotlib.pyplot as plt
#variables
G=nx.Graph()
#asignas la cantidad de nodos
G.add_nodes_from([1,2,3,4])
#asigna las conexiones o aristas
G.add_edges_from([(1,2),(2,3),(3,4),(4,1),(2,4)])
#muestra la cant. de nodos
print("nodos del grafo: ",G.nodes())
#muestra la cant. aristas
print("aristas del grafo: ",G.edges())
#muestra los vecinos del nodo 1
print("Los vecinos de 1 en G son ",(list(G.adj[1])))
#muestra los vecinos del nodo 4
print("Los vecinos de 4 en G son ",(list(G.adj[4])))
#asigno el nodo inicial de la busqueda
source=1
#asigno el nodo de busqueda
target=3
#realiza la busqueda
all_shortest_paths=list(nx.all_shortest_paths(G, source=source, target=target))
#imprime el camino
print(f"el camino mas corto entre {source} y {target}: ",all_shortest_paths)
#muestra el grafico
nx.draw(G,with_labels=True)
plt.show()