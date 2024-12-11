with open("input.txt", "r") as f:
    a = [int(x) for x in f.readline().split()]

# Solve recursively with memoization
T = {}

def blink(x, n):
    if (x, n) in T:
        return T[(x, n)]
    if n == 0:
        res = 1
    elif x == 0:
        res = blink(1, n-1)
    else:
        s = str(x)
        l = len(s)
        if l % 2 == 0:
            res1 = blink(int(s[:l//2]), n-1)
            res2 = blink(int(s[l//2:]), n-1)
            res = res1 + res2
        else:
            res = blink(x * 2024, n-1)
    T[(x, n)] = res
    return res

res = 0
for x in a:
    res += blink(x, 75)
print(res)
