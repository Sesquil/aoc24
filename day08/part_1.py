with open("input.txt", "r") as f:
    level = [line.strip() for line in f.readlines()]

n, m  = len(level), len(level[0])
sym = {c for c in "".join(level) if c != "."}
pos = {c: [(x, y) for x in range(m) for y in range(n) if level[y][x] == c] for c in sym}

def check_pos(x, y):
    return x >= 0 and x < m and y >= 0 and y < n

antipos = set()
for c, p in pos.items():
    for i in range(len(p)-1):
        for j in range(i+1, len(p)):
            dx, dy = p[j][0] - p[i][0], p[j][1] - p[i][1]
            for k in (-1, 2):
                x, y = p[i][0] + k*dx, p[i][1] + k*dy
                if check_pos(x, y):
                    antipos.add((x, y))

#print("\n".join("".join("#" if (x, y) in antipos else level[y][x] \
#      for x in range(m)) for y in range(n)))

res = len(antipos)
print(res)
