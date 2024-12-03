# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import networkx as nx
import matplotlib . pyplot as plt
import numpy as np 


#G = nx.Graph()#creer un graphe non oriente
#G.add_nodes_from(["a","b","c","d","e","f"])
#G.add_edges_from([("a","c"),("f","d"),("a","e"),("f","b"),("b","d"),("c","e")])
#nx.draw(G,with_labels=True)
#plt.show()
#position = {'a':[0,0],'b':[1,0],'c':[1,1],'d':[0,1],'e':[-1,1],'f':[-1,0],'g':[-1,-1],'h':[0,-1],'i':[1,-1]}
#nx.draw(G,with_labels=True,pos=position)
#plt.show()

#position = {'a':[1,1],'b':[0,3],'c':[-1,1],'d':[-1,-1],'e':[0,-3],'f':[1,-1]}
#nx.draw(G,with_labels=True,pos=position)
#plt.show()
#G = nx.Graph()#creer un graphe non oriente
#G.add_nodes_from(["a","b","c","d"])
#G.add_edges_from([("b","a"),("c","b"),("a","d"),("b","d"),("d","c")])
#G1 = nx.DiGraph()
#G1.add_nodes_from([1,2,3,4,5])
#G1.add_edges_from([(1,5),(1,3),(4,2),(5,2),(3,5)])
G2 = nx.DiGraph()
G2.add_nodes_from([1,2,"a","b"])
G2.add_edges_from([("a",2),(1,"b"),("b","a"),(1,2)])
fig,(ax1,ax2,ax3) = plt.subplots(1,3)
nx.draw(G,with_labels=True,ax=ax1,node_color='red',edge_color='blue',node_size=500)
ax1.set_title('GRAPHE1')
nx.draw(G1,with_labels=True,ax=ax2,node_color='red',edge_color='blue',node_size=500)
ax2.set_title('GRAPHE2')
nx.draw(G2,with_labels=True,ax=ax3,node_color='red',edge_color='blue',node_size=500)
ax3.set_title('GRAPHE3')
plt.tight_layout()
plt.show ()