import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
def gestcomplet(graphe):
    for i in graphe.nodes():
      for j in graphe.nodes():
        if i != j and not graphe.has_edge(i,j):
          return False
    return True 
M = np.array([[0,1,1,1,1,1,1],[1,0,1,1,1,1,1],[1,1,0,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,0,1,1],[1,1,1,1,1,0,1],[1,1,1,1,1,1,0]])
#M = np.array([[0,1,1,1,0,0,0],[1,0,1,0,1,0,0],[1,1,0,0,0,0,0],[0,0,0,0,0,0,1],[0,1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0]])
G=nx.Graph(M)
nx.draw(G , with_labels=True)
plt.show()
if gestcomplet(G):
   print("Le graphe est complet")
else:
   print("Le graphe n'est pas complet")

