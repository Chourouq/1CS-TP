import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def gestsymetrique(graphe):
    for i in graphe.nodes():
        vois= list(graphe.neighbors(i))
        for voisin in vois:
          if i not in graphe.neighbors(voisin):
              return False
    return True

#g_symétrique
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2),(2, 1), (2, 3),(3,2), (3, 1),(1,3)])
#g_ non _symétrique
#G=nx.DiGraph()
#G.add_nodes_from([1,2,3,4])
#G.add_edges_from([(1,2),(2,3),(2,1),(3,4)])
nx.draw(G, with_labels=True)
plt.show()
 
if gestsymetrique(G):
   print("Le graphe est symétrique.")
else:
   print("Le graphe n'est pas symétrique.")
 