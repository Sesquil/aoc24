with open("input.txt", "r") as f:
    lines = f.readlines()

lists = [[], []]
for line in lines:
    for i, x in enumerate(line.split()):
        lists[i].append(int(x))

x_max = max(max(l) for l in lists)
c = [0]*(x_max+1)
for x in lists[1]:
    c[x] += 1
res = sum(x * c[x] for x in lists[0])
print(res)
