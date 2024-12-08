with open("input.txt", "r") as f:
    lines = f.readlines()

def solve(x, a, y, i):
    if i == len(a):
        return x == y
    if y > x:
        return False
    return solve(x, a, y + a[i], i+1) or \
           solve(x, a, y * a[i], i+1) or \
           solve(x, a, int(f"{y}{a[i]}"), i+1)

res = 0
for line in lines:
    x, *a = (int(s) for s in line.replace(":", "").split())
    if solve(x, a, a[0], 1):
        res += x
print(res)
