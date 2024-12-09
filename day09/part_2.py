from itertools import accumulate

with open("input.txt", "r") as f:
    line = f.readline().strip()

a = [int(line[i]) for i in range(0, len(line), 2)]
b = [int(line[i]) for i in range(1, len(line), 2)]
pos_a = [0] + list(accumulate(x + y for x, y in zip(a, b)))
pos_b = [pos_a[i] + a[i] for i in range(len(b))]

for j in range(len(a)-1, 0, -1):
    i = 0
    while i < len(b) and pos_b[i] < pos_a[j] and b[i] < a[j]:
        i += 1
    if i < len(b) and pos_b[i] < pos_a[j] and b[i] >= a[j]:
        pos_a[j] = pos_b[i]
        pos_b[i] += a[j]
        b[i] -= a[j]

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
