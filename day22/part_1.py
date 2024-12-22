with open("input.txt", "r") as f:
    lines = f.readlines()

def next_number(n):
    n = (n ^ (n << 6)) % 16777216
    n = (n ^ (n >> 5)) % 16777216
    n = (n ^ (n << 11)) % 16777216
    return n

res = 0
for line in lines:
    n = int(line)
    for i in range(2000):
        n = next_number(n)
    res += n
    #print(line.strip() + ":", n)
print(res)
