#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 14:55:54 2023

@author: aicha
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
M=np.array([[0,1,0,1],[1,0,0,1],[0,0,0,1],[1,1,0,0]])
G=nx.Graph(M)
nx.draw(G,with_labels=True)
plt.show()
