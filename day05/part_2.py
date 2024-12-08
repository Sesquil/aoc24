from collections import deque

# Compute topologic ordering of given nodes
def topsort(nodes):
    din = {x: 0 for x in nodes}
    for x in nodes:
        for y in adj.get(x , []):
            if y in nodes:
                din[y] +=1
    ordered_nodes = []
    queue = deque([x for x in nodes if din[x] == 0])
    while queue or len(ordered_nodes) != len(nodes):
        x = queue.popleft()
        ordered_nodes.append(x)
        for y in adj.get(x , []):
            if y in nodes:
                din[y] -= 1
                if din[y] == 0:
                    queue.append(y)
    return ordered_nodes

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
adj = {x: [] for x, _ in rules}
for x, y in rules:
    adj[x].append(y)

# Check invalid updates
res = 0
for update in updates:
    pos = {x: i for i, x in enumerate(update)}
    if not all(all(pos[y] > pos[x] for y in adj.get(x, []) if y in pos) for x in update):
        update = topsort(update)
        res += update[len(update)//2]
print(res)
