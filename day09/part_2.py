from itertools import accumulate
from heapq import *

with open("input.txt", "r") as f:
    line = f.readline().strip()

a = [int(line[i]) for i in range(0, len(line), 2)]
b = [int(line[i]) for i in range(1, len(line), 2)]
pos_a = [0] + list(accumulate(x + y for x, y in zip(a, b)))
pos_b = [pos_a[i] + a[i] for i in range(len(b))]
gaps = [[pos_b[i] for i, y in enumerate(b) if y == k] for k in range(10)]
for g in gaps:
    heapify(g)

for j in range(len(a)-1, 0, -1):
    k_min, pos_min = 0, pos_a[j]
    for k in range(a[j], 10):
        if gaps[k] and gaps[k][0] < pos_min:
            k_min, pos_min = k, gaps[k][0]
    if k_min > 0:
        pos_a[j] = pos_min
        heappop(gaps[k_min])
        if k_min > a[j]:
            heappush(gaps[k_min - a[j]], pos_min + a[j])

res = sum(sum(j * (pos_a[j]+k) for k in range(a[j])) for j in range(len(a)))
print(res)

"""
blocks = ["."]*sum(int(c) for c in line)
for i in range(len(a)):
    for j in range(pos_a[i], pos_a[i] + a[i]):
        blocks[j] = str(i)
blocks = "".join(blocks)
print(blocks)
"""
