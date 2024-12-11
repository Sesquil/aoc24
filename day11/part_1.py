with open("input.txt", "r") as f:
    a = [int(x) for x in f.readline().split()]

# Brute-force simulation without optimization
def blink(a):
    b = []
    for x in a:
        if x == 0:
            b.append(1)
        else:
            s = str(x)
            l = len(s)
            if l % 2 == 0:
                b.append(int(s[:l//2]))
                b.append(int(s[l//2:]))
            else:
                b.append(x * 2024)
    return b

for _ in range(25):
    a = blink(a)
    #print(a)

res = len(a)
print(res)
