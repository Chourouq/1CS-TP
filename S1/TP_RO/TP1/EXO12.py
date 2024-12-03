import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
 
def gesttransitif(graphe):
  for a in graphe.nodes():
   for b in graphe.nodes():
    if a != b:
      for c in graphe.nodes():
         if a != c and b != c:
          if nx.has_path(graphe,a,c) and nx.has_path(graphe,c,b):
             if not graphe.has_edge(a,b):
                return False
  return True
G = nx.DiGraph()
G.add_nodes_from([1, 2, 3])
G.add_edges_from([(1, 2), (2, 3), (1, 3)])
  #non transitif\n",
 #G = nx.DiGraph()
 #G.add_nodes_from([1,2,3,4])
 #G.add_edges_from([(1,2),(2,3),(1,3),(1,4),(4,2)])
nx.draw(G, with_labels=True)
plt.show()
if gesttransitif(G):
   print("Le graphe est transitif.")
else:
    print("Le graphe n'est pas transitif.")
