import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
G = nx.DiGraph()
graph = {'a':['b','c'],'b':['a','c'],'c':['b']}
G = nx.DiGraph(graph)
nx.draw(G, with_labels=True)
plt.show ()
nodes = list (G.nodes)
num_nodes = len(nodes)
M = np.array(([[0,0,0],[0,0,0],[0,0,0]]))
for i in range (num_nodes):
  for j in range (num_nodes):
      if G.has_edge(nodes[i],nodes[j]):
          M[i,j]=1
print(M) 

print('la matrice au carre ')
matrice2 = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]

for i in range(len(M)):
   for j in range(len(M[0])):
       for k in range(len(matrice2)):
                matrice2[i][j] += M[i][k] * M[k][j]

   for ligne in matrice2:
       
     print(ligne)
     
print("la matrice cube")
matrice3 = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
for i in range(len(matrice2)):
   for j in range(len(M[0])):
       for k in range(len(matrice2)):
                matrice3[i][j] += matrice2[i][k] * M[k][j]

for ligne in matrice3:
       
      print(ligne)  
     
print("la matrice au puissance 4")

matrice4 = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
for i in range(len(matrice3)):
   for j in range(len(M[0])):
       for k in range(len(matrice2)):
                matrice4[i][j] += M[i][k] * matrice3[k][j]

for ligne in matrice4:
       
      print(ligne)
     
print('la somme de M + M1 + M3 + M4')
matrice5 = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
for i in range(len(M)):
         for j in range(len(M[0])):
             matrice5[i][j] = M[i][j] + matrice2[i][j]+ matrice3[i][j]+ matrice4[i][j]

for ligne in matrice5:
        print(ligne)  
          
#print("la somme des quatres matrices")
#matrice7 = [[0 for _ in range(num_nodes)] for _ in range(num_nodes)]
#for i in range(len(matrice6)):
        #for j in range(len(M[0])):
            #matrice7[i][j] = matrice6[i][j] + M[i][j]

#for ligne in matrice7:
      # print(ligne)  

      