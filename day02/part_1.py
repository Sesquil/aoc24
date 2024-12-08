with open("input.txt", "r") as f:
    lines = f.readlines()

def check_levels(levels, sign):
    n = len(levels)
    if all(0 < sign*(line[i] - line[i-1]) <= 3 for i in range(1, n)):
        return True

res = 0
for line in lines:
    line = [int(x) for x in line.split()]
    n = len(line)
    if check_levels(line, 1) or check_levels(line, -1):
        res += 1

print(res)
