#程序文件Pex10_2_2.py
import networkx as nx
import pylab as plt
import numpy as np
List=[(1,2,9),(1,3,2),(1,4,4),(1,5,7),
  (2,3,3),(2,4,4),(3,4,8),(3,5,4),(4,5,6)]
G=nx.Graph()
G.add_nodes_from(range(1,6))
G.add_weighted_edges_from(List)
pos=nx.shell_layout(G)
w = nx.get_edge_attributes(G,'weight')
nx.draw(G, pos,with_labels=True, font_weight='bold',font_size=12)
nx.draw_networkx_edge_labels(G,pos,edge_labels=w)
plt.show()
