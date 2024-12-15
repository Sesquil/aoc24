level = []
with open("input.txt", "r") as f:
    while line := f.readline().strip():
        level.append([c for c in line])
    moves = ""
    while line := f.readline().strip():
        moves += line

h, w = len(level), len(level[0])
px, py = next((level[y].index("@"), y) for y in range(h) if "@" in level[y])

# Simulate robot movement
STEP = {"^": (0,-1), ">": (1,0), "v": (0,1), "<": (-1,0)}
for m in moves:
    make_move = False
    dx, dy = STEP[m]
    nx, ny = px+dx, py+dy
    if level[ny][nx] == ".":
        make_move = True
    elif level[ny][nx] == "O":
        # Try to push boxes
        k = 1
        while level[ny+k*dy][nx+k*dx] == "O":
            k +=1
        if level[ny+k*dy][nx+k*dx] == ".":
            make_move = True
            level[ny+k*dy][nx+k*dx] = "O"
    # Move robot
    if make_move:
        level[py][px] = "."
        px, py = nx, ny
        level[py][px] = "@"
    # Display level
    #print(f"Move {m}:\n" + "\n".join("".join(row) for row in level) + "\n")

# Compute GPS coordinates
res = sum(sum(100*y+x for x in range(w) if level[y][x] == "O") for y in range(h))

print(res)
