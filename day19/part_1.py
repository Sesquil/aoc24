with open("input.txt", "r") as f:
    lines = f.readlines()

towels = [s.strip() for s in lines[0].split(",")]

def solve(t_list, d):
    # Build graph
    n = len(d)
    adj = [[] for _ in range(n)]
    for t in t_list:
        for i in range(len(d)-len(t)+1):
            if d[i:i+len(t)] == t:
                adj[i].append(i+len(t))
    # Find path via DFS
    visited = [False]*n
    visited[0] = True
    stack = [0]
    while stack:
        i = stack.pop()
        for j in adj[i]:
            if j == n:
                return True
            if not visited[j]:
                visited[j] = True
                stack.append(j)
    return False

res = 0
for design in (s.strip() for s in lines[2:]):
    if solve(towels, design):
        res += 1
print(res)
