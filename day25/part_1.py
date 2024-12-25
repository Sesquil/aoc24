with open("input.txt", "r") as f:
    blocks = [b.split() for b in "".join(f.readlines()).split("\n\n")]

# Read schematics
N, M = 5, 5
keys = []
locks = []
for b in blocks:
    s = [sum(1 for y in range(1,N+1) if b[y][x] == "#") for x in range(M)]
    if b[0][0] == "#":
        locks.append(s)
    else:
        keys.append(s)

# Count key/lock combinations
res = 0
for k in keys:
    for l in locks:
        if all(k[i] + l[i] <= N for i in range(M)):
            res += 1
print(res)
