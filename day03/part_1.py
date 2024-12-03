import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

regexp = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
res = 0
for line in lines:
    for m in regexp.findall(line):
        res += int(m[0]) * int(m[1])

print(res)
