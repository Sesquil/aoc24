import re

def parseTests(f):
    regexp = re.compile(r"\d+")
    tests = []
    while True:
        lines = [f.readline() for _ in range(4)]
        if not lines[0]: break
        tests.append([tuple(int(z) for z in regexp.findall(l)) for l in lines[:-1]])
        tests[-1][-1] = tuple(10000000000000 + z for z in tests[-1][-1])
    return tests

with open("input.txt", "r") as f:
    tests = parseTests(f)

# Solve linear equation system [a b] x = p
def solve(a, b, p):
    A = [[a[0], b[0]], [a[1], b[1]]]
    d = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    Ainv = [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]
    i = (Ainv[0][0]*p[0] + Ainv[0][1]*p[1]) / d
    j = (Ainv[1][0]*p[0] + Ainv[1][1]*p[1]) / d
    return 3*round(i) + round(j) if max(abs(i-round(i)), abs(j-round(j))) < 1e-6 else 0

res = 0
for t in tests:
    res += solve(*t)
print(res)
