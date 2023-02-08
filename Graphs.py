
#Useful resources: 
#https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
#https://stackoverflow.com/questions/40040304/creating-weighted-directed-graph-in-python-based-on-user-input

#https://github.com/networkx/networkx
#Environment preparation: pip install networkx

import networkx as nx   #advised naming convention

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


#LAB 4.2 Example
example = { "START" : {"A", "C"},
      "A" : {"B", "D"},
      "B" : {"META"},
      "C" : {"D"},
      "D" : {"B", "META"},
      "META" : {}
    }
example2=[
    ("START", "A", 5), 
    ("START", "C",6),
    ("A","B",1),
    ("A","D",2),
    ("C","D",8),
    ("B","META",6),
    ("D","B",7),
    ("D","META",3)
]

FG = nx.Graph()

FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])

for n, nbrs in FG.adj.items():

   for nbr, eattr in nbrs.items():

       wt = eattr['weight']

       if wt < 0.5: print(f"({n}, {nbr}, {wt:.3})")