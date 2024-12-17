with open("input.txt", "r") as f:
    lines = f.readlines()

# Initialize state
reg = [int(line.split()[-1]) for line in lines[:3]]
prg = [int(x) for x in lines[4][9:-1].split(",")]

# Define instructions
def get_op(x):
    return x if x < 4 else reg[x-4]
def ins_adv(x):
    reg[0] //= (1 << get_op(x))
def ins_bxl(x):
    reg[1] ^= x
def ins_bst(x):
    reg[1] = get_op(x) & 7
def ins_jnz(x):
    global ptr
    if reg[0] != 0:
        ptr = x-2
def ins_bxc(x):
    reg[1] ^= reg[2]
def ins_out(x):
    out.append(get_op(x) & 7)
def ins_bdv(x):
    reg[1] = reg[0] // (1 << get_op(x))
def ins_cdv(x):
    reg[2] = reg[0] // (1 << get_op(x))

INS = [ins_adv, ins_bxl, ins_bst, ins_jnz, ins_bxc, ins_out, ins_bdv, ins_cdv]

def check(bits, idx, val):
    next_bits = None
    vals = [1 if val & k else 0 for k in (4, 2, 1)]
    if all(bits[idx+i] < 0 or bits[idx+i] == v for i, v in enumerate(vals) if idx+i >= 0):
        next_bits = bits[:]
        for i, v in enumerate(vals):
            if idx+i >= 0:
                next_bits[idx+i] = v
    return next_bits

solutions = []

def solve(bits, i):
    if i == 16:
        a = int("".join(map(str, bits)), 2)
        solutions.append(a)
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
solve([-1]*48, 0)
res = 0
for a in solutions:
    # Simulate program execution for verification
    reg = [a, 0, 0]
    out = []
    ptr = 0
    while ptr < len(prg):
        INS[prg[ptr]](prg[ptr+1])
        ptr += 2
    if out == prg:
        res = min(res, a) if res > 0 else a

print(res)

"""
Program:
B = A & 7
B = B ^ 1
C = A // (2 ** B) = A >> B
B = B ^ 5
B = B ^ C
A = A // 8
out B & 7
jmp 0

out: (a ^ 4) ^ (a >> (a ^ 1))

abcdefg000 >> 001 = g00
abcdefg001 >> 000 = 001
abcdefg010 >> 011 = efg
abcdefg011 >> 010 = fg0
abcdefg100 >> 101 = cde
abcdefg101 >> 100 = def
abcdefg110 >> 111 = abc
abcdefg111 >> 110 = bcd

in = xyz, out = klm

xyz = 000 => 100 ^ g00 = G00     g = K, lm = 00
xyz = 001 => 101 ^ 001 = 100     klm = 100
xyz = 010 => 110 ^ efg = EFg     efg = KLm
xyz = 011 => 111 ^ fg0 = FG1     fg = KL, m = 1
xyz = 100 => 000 ^ cde = cde     cde = klm
xyz = 101 => 001 ^ def = deF     def = klM
xyz = 110 => 010 ^ abc = aBc     abc = kLm
xyz = 111 => 011 ^ bcd = bCD     bcd = kLM
"""
