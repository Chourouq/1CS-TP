import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

G = nx.DiGraph()
G.add_nodes_from([1, 2, 3,4,5,6,7,8])
graph={1:[2,8],2:[4,5,6],3:[],4:[3],5:[3,7],6:[],7:[1],8:[1]}
G = nx.DiGraph(graph)
nx.draw(G, with_labels=True)
plt.show ()
nodes = list (G.nodes)
num_nodes = len(nodes)
M = nx.to_numpy_array(G)
V = np.array(([[0,0,0,0,0,0,0,0]]))

for i in range(len(M)):
       for j in range(len(M[0])):
           for k in range(len(V)):
                  V[k] += M[j]

       for ligne in V:
           
         print(ligne)
   
