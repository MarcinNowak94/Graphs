
#Useful resources: 
#https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
#https://stackoverflow.com/questions/40040304/creating-weighted-directed-graph-in-python-based-on-user-input

#https://github.com/networkx/networkx
#Environment preparation: pip install networkx

import matplotlib.pyplot as plt
import networkx as nx   #advised naming convention


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def DisplayGraph(graph, pos):
    
    #pos = nx.spring_layout(graph, seed=3068)  # Seed layout for reproducibility
    nx.draw(graph, pos=pos, with_labels=True)
    #plt.title(label="Graf")
    plt.show()


#LAB 4.2 Example
example=[
    ("START", "A", 5),
    ("START", "C",6),
    ("A","B",1),
    ("A","D",2),
    ("C","D",8),
    ("B","META",6),
    ("D","B",7),
    ("D","META",3)
]
pos={
    "START": [-2, 0],
    "A":    [-1,1],
    "B":    [1,1],
    "C":    [-1,-1],
    "D":    [1,-1],
    "META":    [2,0]
}
G = nx.DiGraph(name="Graf")

G.add_weighted_edges_from(example)

pathlengths = []

print("source vertex {target:length, }")
for v in G.nodes():
    spl = dict(nx.single_source_shortest_path_length(G, v))
    print(f"{v} {spl} ")
    for p in spl:
        pathlengths.append(spl[p])

print()
print(f"average shortest path length {sum(pathlengths) / len(pathlengths)}")

# histogram of path lengths
dist = {}
for p in pathlengths:
    if p in dist:
        dist[p] += 1
    else:
        dist[p] = 1

print()
print("length #paths")
verts = dist.keys()
for d in sorted(verts):
    print(f"{d} {dist[d]}")

#print(nx.is_connected(G))
#print(f"radius: {nx.radius(G)}")
#print(f"diameter: {nx.diameter(G)}")
#print(f"eccentricity: {nx.eccentricity(G)}")
#print(f"center: {nx.center(G)}")
#print(f"periphery: {nx.periphery(G)}")
#print(f"density: {nx.density(G)}")

DisplayGraph(G, pos)