import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
def gestreflexif(graphe):
    for i in graphe.nodes():
        if not graphe.has_edge(i,i):
            return False
    return True    
 
M = np.array([[0,1,1,1,0,0,0],[1,1,1,0,1,0,0],[1,1,1,0,0,0,0],[0,0,0,1,0,0,1],[0,1,0,0,1,0,0],[0,0,0,0,0,1,0],[0,0,0,1,0,0,1]])
G=nx.Graph(M)
nx.draw(G , with_labels=True)
plt.show()
if gestreflexif(G):
   print("Le graphe est reflexif")
else:
     print("Le graphe n'est pas reflexif ") 

  
  