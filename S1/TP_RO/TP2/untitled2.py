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
print('la matrice transitive ')
A = nx.to_numpy_array(G)
M = A
for k in range (num_nodes):
     for i in range (num_nodes):
         for j in range (num_nodes):
             M[i,j]=  M[i,j] or ( M[i,k] and  M[k,j])
 
for ligne in M:
    print(ligne)