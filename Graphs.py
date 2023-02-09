
#Useful resources: 
#https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs
#https://stackoverflow.com/questions/40040304/creating-weighted-directed-graph-in-python-based-on-user-input

#https://github.com/networkx/networkx
#Environment preparation: pip install networkx

import matplotlib.pyplot as plt
import networkx as nx   #advised naming convention
import time
import sys

Config={
    "NodeSize": 700,
    "EdgeWidth": 2,
    "EmphasizedEdgeWidth": 6,
    "FontSize": 15,
    "FontFamily": "sans-serif"
}

#-------------------------------------------------------------------------------
#Opis algorytmu krok po kroku:
#Każdy wierzchołek oznacz kosztem MINIMALNYM, wierzchołek START kosztem 0
#Zacznij od punktu START
#Przejdź do kolejnego wierzchołka pierwszą dostępną krawędzią.
#Oblicz koszt ścieżki jako koszt punktu z którego wychodzi krawędź + koszt krawędzi
#Jeśli koszt ścieżki jest większy niż koszt wierzchołka przypisz wierzchołkowi koszt ścieżki i zapisz pełną ścieżkę od punktu START z nim związaną 
#Powtarzaj dla każdego wierzchołka do momentu obliczenia wszystkich ścieżek
#Zapisana ścieżka o najwyższym koszcie jest ścieżką krytyczną
#-------------------------------------------------------------------------------

def CalculateCriticalPath(graph, startnode, endnode):
    G=graph #local copy for modification
    emph={
        "src":"",
        "dst":""
    }
    
    criticalpaths={}
    for node in G.nodes:
        criticalpaths[node]={
            "cost":-sys.maxsize,
            "path":node, 
            "inputs":G.in_degree[node], 
            "visited":False}
    criticalpaths[startnode]={"cost":0,"path":startnode}

    #TODO: to fix create Breadth-first queue https://pl.wikipedia.org/wiki/Sortowanie_topologiczne
    for (node, out) in G.out_degree:
        edges=[(src, dst, cost) for (src, dst, cost) in G.edges(data=True) if src==node]
        #print("---------Current node: "+node+"----------------")
        for (start, end, weight) in edges:
            cost=weight["weight"]
            print(start+end+" weight:"+str(cost))
            if (criticalpaths[end]["cost"]<cost):
                criticalpaths[end]={
                    "cost":criticalpaths[start]["cost"]+cost,
                    "path":criticalpaths[start]["path"]+"->"+end
                    }
            #print(criticalpaths)
            DisplayGraph(G, pos, {"src":start,"dst":end})
        print("Critical path from node "+startnode+" to node " +endnode+ " is: "+criticalpaths[endnode]["path"]+" its cost is "+str(criticalpaths[endnode]["cost"])+".")
    print("Not ready yet, please come again later\n")
#-------------------------------------------------------------------------------
def DisplayGraphData(G, issimple):
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

    if (issimple==True):
        print(nx.is_connected(G))
        print(f"radius: {nx.radius(G)}")
        print(f"diameter: {nx.diameter(G)}")
        print(f"eccentricity: {nx.eccentricity(G)}")
        print(f"center: {nx.center(G)}")
        print(f"periphery: {nx.periphery(G)}")
        print(f"density: {nx.density(G)}")

#TODO: nicely step over, currently 
def DisplayGraph(G, pos, emph):
    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=Config["NodeSize"])

    # edges
    edges = [(u, v) for (u, v, d) in G.edges(data=True) if not(u==emph["src"] and v==emph["dst"])]
    enlarged = [(u, v) for (u, v, d) in G.edges(data=True) if (u==emph["src"] and v==emph["dst"])]
    
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=Config["EdgeWidth"])
    nx.draw_networkx_edges(G, pos, edgelist=enlarged, width=Config["EmphasizedEdgeWidth"])

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
issimplegraph=False
G.add_weighted_edges_from(example)

#DisplayGraphData(G, issimplegraph)

emph={
    "src":"",
    "dst":""
}
#DisplayGraph(G, pos, emph)

CalculateCriticalPath(G, "START", "META")