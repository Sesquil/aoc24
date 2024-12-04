with open('input.txt', 'r') as f:
    lines = f.readlines()

DIRS = [(-1, -1), (1, -1), (-1, 1), (1, 1)]
VALID = ["MMSS", "SSMM", "MSMS", "SMSM"]

def find_xmas(x, y, w, h):
    if lines[y][x] != "A":
        return 0
    s = "".join(lines[y+dy][x+dx] for dx, dy in DIRS)
    return 1 if s in VALID else 0

res = 0
h, w = len(lines), len(lines[0])
for y in range(1, h-1):
    for x in range(1, w-1):
        res += find_xmas(x, y, w, h)

print(res)
