with open("input.txt", "r") as f:
    lines = f.readlines()

lists = [[], []]
for line in lines:
    for i, x in enumerate(line.split()):
        lists[i].append(int(x))

for l in lists:
    l.sort()

res = sum(abs(x - y) for x, y in zip(*lists))
print(res)
