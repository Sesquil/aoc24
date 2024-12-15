level = []
with open("input.txt", "r") as f:
    while line := f.readline().strip():
        row = []
        for c in line:
            if c == "O":
                row.append("["); row.append("]")
            else:
                row.append(c); row.append(c)
        level.append(row)
    moves = ""
    while line := f.readline().strip():
        moves += line

h, w = len(level), len(level[0])
px, py = next((level[y].index("@"), y) for y in range(h) if "@" in level[y])
level[py][px+1] = "."

# Check recursively if box is pushable into direction
def pushable(bx, by, m, boxes):
    if (bx, by) in boxes:
        return boxes[(bx, by)]
    res = True
    if m == "<" or m == ">":
        nx = bx-1 if m == "<" else bx+2
        if level[by][nx] == "#":
            res = False
        elif level[by][nx] in "[]":
            res = pushable(bx-2 if nx < bx else bx+2, by, m, boxes)
    else:  # m == "^" or m == "v"
        ny = by-1 if m == "^" else by+1
        res = True
        for nx in (bx, bx+1):
            if level[ny][nx] == "#":
                res = False
            elif level[ny][nx] == "[":
                res = pushable(nx, ny, m, boxes)
            elif level[ny][nx] == "]":
                res = pushable(nx-1, ny, m, boxes)
            if not res:
                break
    boxes[(bx, by)] = res
    return res

# Simulate robot movement
STEP = {"^": (0,-1), ">": (1,0), "v": (0,1), "<": (-1,0)}
for m in moves:
    make_move = False
    dx, dy = STEP[m]
    nx, ny = px+dx, py+dy
    if level[ny][nx] == ".":
        make_move = True
    elif level[ny][nx] in "[]":
        # Try to push boxes
        boxes = {}
        if pushable(nx if level[ny][nx] == "[" else nx-1, ny, m, boxes):
            for bx, by in boxes:
                level[by][bx] = "."; level[by][bx+1] = "."
            for bx, by in boxes:
                level[by+dy][bx+dx] = "["; level[by+dy][bx+dx+1] = "]"
            make_move = True
    # Move robot
    if make_move:
        level[py][px] = "."
        px, py = nx, ny
        level[py][px] = "@"
    # Display level
    #print(f"Move {m}:\n" + "\n".join("".join(row) for row in level) + "\n")

# Compute GPS coordinates
res = sum(sum(100*y+x for x in range(w) if level[y][x] == "[") for y in range(h))

print(res)
