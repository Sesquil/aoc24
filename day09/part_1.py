with open("input.txt", "r") as f:
    line = f.readline().strip()

a = [int(line[i]) for i in range(0, len(line), 2)]
b = [int(line[i]) for i in range(1, len(line), 2)]
i, j = 0, len(a)-1
x, y = b[i], a[j]
pos = a[0]
res = 0
#blocks = "0" * a[0]
while i < j:
    if x == 0:
        i += 1
        n = a[i] if i < j else y
        #blocks += str(i) * n
        res += sum(i * (pos+k) for k in range(n))
        pos += a[i]
        x = b[i]
    elif y == 0:
        j -= 1
        y = a[j]
    else:
        n = min(x, y)
        #blocks += str(j) * n
        res += sum(j * (pos+k) for k in range(n))
        pos += n
        x -= n
        y -= n

print(res)
#print(blocks.ljust(sum(a) + sum(b), "."))
