with open("input.txt", "r") as f:
    lines = f.readlines()

# Build graph
adj = {}
for line in lines:
    a, b = line.strip().split("-")
    if not a in adj:
        adj[a] = [b]
    else:
        adj[a].append(b)
    if not b in adj:
        adj[b] = [a]
    else:
        adj[b].append(a)

# Find triangles
triangles = set()
for a in adj:
    for b in adj[a]:
        if a < b:
            for c in adj[b]:
                if b < c and a in adj[c]:
                    triangles.add((a, b, c))

res = sum(1 for t in triangles if any(s[0] == "t" for s in t))
print(res)
