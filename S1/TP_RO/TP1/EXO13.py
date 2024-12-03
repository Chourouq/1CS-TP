import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def complementairedeg(graphe):
    complementaire = nx.Graph()
    complementaire.add_nodes_from(graphe.nodes())
    for a in graphe.nodes():
        for b in graphe.nodes():
            if a != b:
                if not graphe.has_edge(a,b):
                    complementaire.add_edge(a,b)
    return complementaire

G = nx.Graph()
G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(2,3),(4,2),(3,5)])
plt.show()
plt.title("Complémentaire du graphe")
nx.draw(complementairedeg(G), with_labels=True,node_color="yellow")
plt.show()