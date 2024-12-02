with open('input.txt', 'r') as f:
    lines = f.readlines()

def check_levels(levels, sign):
    n = len(levels)
    # Compute indices i of levels l_(i-1), l_i where errors occur
    error_idx = [i for i in range(1, n) if not (0 < sign*(line[i] - line[i-1]) <= 3)]
    if len(error_idx) == 0:
        return True
    if len(error_idx) > 2:
        return False
    # Remove i-th level or (i-1)-th level for error at i-th level
    if len(error_idx) == 1:
        i = error_idx[0]
        return i == 1 or 0 < sign*(line[i] - line[i-2]) <= 3 or \
               i == n-1 or 0 < sign*(line[i+1] - line[i-1]) <= 3
    # Remove i-th level for error at i-th and (i+1)-th level
    i, j = error_idx
    if j != i+1:
        return False
    else:
        return 0 < sign*(line[j] - line[j-2]) <= 3

res = 0
for line in lines:
    line = [int(x) for x in line.split()]
    if check_levels(line, 1) or check_levels(line, -1):
        res += 1

print(res)
