with open("input.txt", "r") as f:
    lines = f.readlines()

# Initialize state
reg = [int(line.split()[-1]) for line in lines[:3]]
prg = [int(x) for x in lines[4][9:-1].split(",")]
out = []
ptr = 0

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

# Simulate program execution
while ptr < len(prg):
    INS[prg[ptr]](prg[ptr+1])
    ptr += 2

res = ",".join(map(str, out))
print(res)
