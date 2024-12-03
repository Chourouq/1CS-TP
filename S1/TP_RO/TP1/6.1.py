import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
G= nx.Graph()
G.add_edge(1, 2, weight=0.5)
G.add_edges_from([(1,3,{'weight':0.9}),(2,3,{'weight':0.3})])
pos=nx.spring_layout(G)
nx.draw(G,with_labels=True,pos=pos)
nx.spring_layout
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos,edge_labels=labels)
plt.show()
