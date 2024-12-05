from collections import deque

rules = []
updates = []
process_rules = True
with open('input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if not line:
            process_rules = False
        elif process_rules:
            rules.append(tuple(int(x) for x in line.split("|")))
        else:
            updates.append(tuple(int(x) for x in line.split(",")))

# Create graph from rules
n = 100
adj_out = [[] for _ in range(n)]
d_in = [0]*n
for i, j in rules:
    adj_out[i].append(j)
    d_in[j] += 1

# Compute topologic sorting of nodes with Kahn's algorithm
queue = deque()
for i in range(n):
    if d_in[i] == 0:
        queue.append(i)
node_order = {}
while len(queue) > 0:
    i = queue.popleft()
    node_order[i] = len(node_order)
    for j in adj_out[i]:
        d_in[j] -= 1
        if d_in[j] == 0:
            queue.append(j)

# Check updates
res = 0
for update in updates:
    orders = [node_order[i] for i in update if i in node_order]
    if all(orders[k] < orders[k+1] for k in range(len(orders)-1)):
        res += update[len(update)//2]
print(res)
