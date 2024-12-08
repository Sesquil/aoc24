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

# Check valid updates
res = 0
for update in updates:
    pos = {x: i for i, x in enumerate(update)}
    if all(all(pos[y] > pos[x] for y in adj.get(x, []) if y in pos) for x in update):
        res += update[len(update)//2]
print(res)
