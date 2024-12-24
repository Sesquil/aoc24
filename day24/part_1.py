from collections import deque
import re

with open("input.txt", "r") as f:
    lines = f.readlines()

# Build network
values = {}
regexp = re.compile(r"([^:]+): (0|1)")
for i in range(len(lines)):
    m = regexp.match(lines[i])
    if not m:
        break
    values[m[1]] = int(m[2])

updates = {}
adj_out = {}
d_in = {}
for i in range(i+1, len(lines)):
    in1, op, in2, _, out = lines[i].split()
    updates[out] = (op, in1, in2)
    for u in (in1, in2):
        if not u in adj_out:
            adj_out[u] = [out]
        else:
            adj_out[u].append(out)
        if u in values:
            if not out in d_in:
                d_in[out] = 1
            else:
                d_in[out] += 1

# Simulate network
OPS = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}
todo = deque()
for u in d_in:
    if d_in[u] == 2:
        todo.append(u)
while todo:
    out = todo.popleft()
    op, in1, in2 = updates[out]
    values[out] = OPS[op](values[in1], values[in2])
    for u in adj_out.get(out, []):
        if not u in d_in:
            d_in[u] = 1
        else:
            d_in[u] += 1
            if d_in[u] == 2:
                todo.append(u)

out_vals = (values[u] for u in sorted(values, reverse=True) if u[0] == "z")
res = int("".join(str(x) for x in out_vals), 2)
print(res)
