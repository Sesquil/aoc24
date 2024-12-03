import re

with open('input.txt', 'r') as f:
    lines = f.readlines()

regexp = re.compile(r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))')
res = 0
do = True
for line in lines:
    for m in regexp.findall(line):
        if m[0] == 'do()':
            do = True
        elif m[0] == 'don\'t()':
            do = False
        elif do:
            res += int(m[1]) * int(m[2])

print(res)
