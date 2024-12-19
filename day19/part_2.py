with open("input.txt", "r") as f:
    lines = f.readlines()

towels = [s.strip() for s in lines[0].split(",")]

def solve(t_list, d):
    # Build graph
    n = len(d)
    adj_in = [[] for _ in range(n+1)]
    for t in t_list:
        for i in range(len(d)-len(t)+1):
            if d[i:i+len(t)] == t:
                adj_in[i+len(t)].append(i)
    # Count paths with bottom-up DP
    count = [0]*(n+1)
    count[0] = 1
    for i in range(1, n+1):
        count[i] = sum(count[j] for j in adj_in[i])
    return count[n]

res = 0
for design in (s.strip() for s in lines[2:]):
    res += solve(towels, design)
print(res)
