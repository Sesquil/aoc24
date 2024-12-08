import numpy as np

with open("input.txt", "r") as f:
    lines = f.readlines()

lists = [[], []]
for line in lines:
    for i, x in enumerate(line.split()):
        lists[i].append(int(x))

x_max = max(lists[0])
hists = [np.histogram(l, bins=x_max, range=[0.5, x_max+0.5]) for l in lists]
res = np.dot(hists[0][0], np.multiply(hists[1][0], list(range(1, x_max+1))))
print(res)
