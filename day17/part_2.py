with open("input.txt", "r") as f:
    lines = f.readlines()

# Read program
prg = [int(x) for x in lines[4][9:-1].split(",")]

# Check constraints for bits
def check(bits, idx, val):
    next_bits = None
    vals = [1 if val & k else 0 for k in (4, 2, 1)]
    if all((bits[idx+i] if idx+i >= 0 else 0) in [v, -1] for i, v in enumerate(vals)):
        next_bits = bits[:]
        for i, v in enumerate(vals):
            if idx+i >= 0:
                next_bits[idx+i] = v
    return next_bits

# Solve by propagating bit constraints
def solve(bits, i):
    if i == 16:
        global res
        a = int("".join(map(str, bits)), 2)
        res = min(res, a) if res > 0 else a
        return
    j = 45 - 3*i
    cand = [[0, 1] if bits[j+k] < 0 else [bits[j+k]] for k in range(3)]
    for x in cand[0]:
        bits[j] = x
        for y in cand[1]:
            bits[j+1] = y
            for z in cand[2]:
                bits[j+2] = z
                xyz = 4*x + 2*y + z
                if next_bits := check(bits, j - (xyz ^ 1), (xyz ^ 4) ^ prg[i]):
                    solve(next_bits, i+1)

# Compute register A
res = 0
solve([-1]*48, 0)
print(res)

"""
Program:
0: B = A & 7
1: B = B ^ 1
2: C = A // (2 ** B) = A >> B
3: B = B ^ 5
4: B = B ^ C
5: A = A // 8
6: out B & 7
7: jmp 0

output: (B ^ 4) ^ (A >> (B ^ 1)) with B = A & 7

j-th output klm, j-th last word xyz in register A
with 7 previous bits abcdefg results in (X = not x):

xyz = 000 => 100 ^ gxy = Gxy => gxy = Klm
xyz = 001 => 101 ^ xyz = XyZ => xyz = KlM
xyz = 010 => 110 ^ efg = EFg => efg = KLm
xyz = 011 => 111 ^ fgx = FGX => fgx = KLM
xyz = 100 => 000 ^ cde = cde => cde = klm
xyz = 101 => 001 ^ def = deF => def = klM
xyz = 110 => 010 ^ abc = aBc => abc = kLm
xyz = 111 => 011 ^ bcd = bCD => bcd = kLM
"""
