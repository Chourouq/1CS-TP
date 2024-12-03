import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#THE ORIGINAL ONE 
d={0:[1,3],1:[0,2],3:[1,4],4:[2,0],5:[0,1]}
G=nx.DiGraph(d)
nx.draw(G,with_labels=True)
plt.show()
#THE SECOND ONE
S = [1, 2, 3]
sous_graphe=nx.DiGraph()
sous_graphe.add_nodes_from(S)
edges=list(G.edges)
for i in S:
    for j in S:
        if (i,j)in edges:
            sous_graphe.add_edge(i,j)
nx.draw(sous_graphe, with_labels=True)
plt.show()   