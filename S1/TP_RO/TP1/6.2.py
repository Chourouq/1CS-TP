import networkx as nx
import matplotlib.pyplot as plt
d= {1:{2:{'weight':0.5},3:{'weight':0.9}},2:{3:{'weight':0.3}}}
G= nx.DiGraph(d)
pos=nx.spring_layout(G)
nx.draw(G,with_labels=True,pos=pos)
labels=nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos,edge_labels=labels)
plt.show()
