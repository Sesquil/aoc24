with open("input.txt", "r") as f:
    lines = f.readlines()

def find_str(s, x, y, w, h, dx, dy):
    if lines[y][x] != s[0]:
        return 0
    n = len(s)
    to_x, to_y = x + (n-1)*dx, y + (n-1)*dy
    if to_x < 0 or to_x >= w or to_y < 0 or to_y >= h:
        return 0
    for i in range(1, n):
        x += dx; y += dy
        if lines[y][x] != s[i]:
            return 0
    return 1

DIRS = [(-1, -1), (1, 1), (1, -1), (-1, 1), (1, 0), (-1, 0), (0, 1), (0, -1)]
STR = "XMAS"
res = 0
h, w = len(lines), len(lines[0])
for y in range(h):
    for x in range(w):
        for dx, dy in DIRS:
            res += find_str(STR, x, y, w, h, dx, dy)

print(res)
