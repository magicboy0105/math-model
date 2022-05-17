#程序文件Pex10_3.py
import numpy as np
import networkx as nx
import pylab as plt
G=nx.DiGraph()
List=[(1,2),(1,3),(2,3),(3,2),(3,5),(4,2),(4,6),
      (5,2),(5,4),(5,6),(6,5)]
G.add_nodes_from(range(1,7))
G.add_edges_from(List)
plt.rc('font',size=16)
pos=nx.shell_layout(G) 
nx.draw(G,pos,with_labels=True, font_weight='bold',node_color='r')
plt.savefig("figure10_3.png", dpi=500); plt.show()
