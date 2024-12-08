with open('input.txt', 'r') as f:
    level = [line.strip() for line in f.readlines()]

n, m  = len(level), len(level[0])
sym = {c for c in "".join(level) if c != "."}
pos = {c: [(x, y) for x in range(m) for y in range(n) if level[y][x] == c] for c in sym}

antipos = set()
for c, p in pos.items():
    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            dx, dy = p[j][0] - p[i][0], p[j][1] - p[i][1]
            kx1, kx2 = p[i][0] // abs(dx), (m-1-p[i][0]) // abs(dx)
            ky1, ky2 = p[i][1] // abs(dy), (n-1-p[i][1]) // abs(dy)
            kmin = min(kx1 if dx > 0 else kx2, ky1 if dy > 0 else ky2)
            kmax = min(kx2 if dx > 0 else kx1, ky2 if dy > 0 else ky1)
            for k in range(-kmin, kmax+1):
                x, y = p[i][0] + k*dx, p[i][1] + k*dy
                antipos.add((x, y))

#print("\n".join("".join("#" if (x, y) in antipos else level[y][x] \
#      for x in range(m)) for y in range(n)))

res = len(antipos)
print(res)
