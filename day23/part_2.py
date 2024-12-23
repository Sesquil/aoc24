import networkx as nx

with open("input.txt", "r") as f:
    lines = f.readlines()

# Build graph
G = nx.Graph()
nodes = set()
for line in lines:
    a, b = line.strip().split("-")
    if not a in nodes:
        G.add_node(a)
    if not b in nodes:
        G.add_node(b)
    G.add_edge(a, b)

# Find max clique
cliques = list(nx.find_cliques(G))
cliques.sort(key=lambda c: len(c), reverse=True)

res = ",".join(sorted(x for x in cliques[0]))
print(res)
