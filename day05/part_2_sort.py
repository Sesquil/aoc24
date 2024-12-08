# Node class with gt operator for topologic sort
class Node:
    def __init__(self, x):
        self.val = x
        self.adj = []
    def __gt__(self, other):
        return other.val in self.adj

rules = []
updates = []
process_rules = True
with open("input.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            process_rules = False
        elif process_rules:
            rules.append([int(x) for x in line.split("|")])
        else:
            updates.append([int(x) for x in line.split(",")])

# Create graph from rules (out adjacency lists)
nodes = {x: Node(x) for x, _ in rules}
for x, y in rules:
    nodes[x].adj.append(y)

# Check invalid updates
res = 0
for update in updates:
    pos = {x: i for i, x in enumerate(update)}
    if not all(all(pos[y] > pos[x] for y in nodes[x].adj if y in pos) for x in update):
        update_nodes = [nodes[x] for x in update]
        update_nodes.sort()
        res += update_nodes[len(update)//2].val
print(res)
