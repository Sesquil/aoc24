with open("input.txt", "r") as f:
    lines = f.readlines()

def next_number(n):
    n = (n ^ (n << 6)) % 16777216
    n = (n ^ (n >> 5)) % 16777216
    n = (n ^ (n << 11)) % 16777216
    return n

prices = {}
for line in lines:
    n = int(line)
    p = n % 10
    seq = (0,)*4
    found_seq = set()
    for i in range(2000):
        n = next_number(n)
        dp = n % 10 - p
        p = n % 10
        seq = seq[1:] + (dp,)
        if i >= 3 and not seq in found_seq:
            if not seq in prices:
                prices[seq] = p
            else:
                prices[seq] += p
            found_seq.add(seq)

res = max(prices.values())
print(res)
