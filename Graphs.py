
#Useful resources: 
#https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
#https://stackoverflow.com/questions/40040304/creating-weighted-directed-graph-in-python-based-on-user-input

#https://github.com/networkx/networkx
#Environment preparation: pip install networkx

import matplotlib.pyplot as plt
import networkx as nx   #advised naming convention

Config={
    "NodeSize": 700,
    "EdgeWidth": 3,
    "FontSize": 15,
    "FontFamily": "sans-serif"
}

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
def DisplayGraph(G, pos):
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=Config["NodeSize"])

    # edges
    edges = [(u, v) for (u, v, d) in G.edges(data=True)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=Config["EdgeWidth"])

    # node labels
    nx.draw_networkx_labels(G, pos, font_size=Config["FontSize"], font_family=Config["FontFamily"])
    # edge weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    ax = plt.gca()
    ax.margins(0.08)
    ax.set_title(G.name)
    plt.axis("off")
    plt.tight_layout()
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