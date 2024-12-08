with open("input.txt", "r") as f:
    lines = f.readlines()

lists = [[], []]
for line in lines:
    for i, x in enumerate(line.split()):
        lists[i].append(int(x))

for l in lists:
    l.sort()

res = 0
i, j = 0, 0
n, m = (len(l) for l in lists)
a, b = (l for l in lists)
while i < n:
    x = a[i]
    c = 0
    while i < n and x == a[i]:
        c += 1
        i += 1
    while j < m and b[j] < x:
        j += 1
    d = 0
    while j < m and b[j] == x:
        d += 1
        j += 1
    res += c * x * d
print(res)
