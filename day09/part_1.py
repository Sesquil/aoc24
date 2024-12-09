with open("input.txt", "r") as f:
    line = f.readline().strip()

i = 1
j = len(line)-1
x = int(line[i])
y = int(line[j])
fid = j // 2
pos = int(line[0])
res = 0
#blocks = "0" * int(line[0])
while i < j:
    if x == 0:
        n = int(line[i+1]) if i+1 < j else y
        #blocks += str((i+1)//2) * n
        res += sum(((i+1)//2) * (pos+k) for k in range(n))
        pos += int(line[i+1])
        i += 2
        x = int(line[i])
    elif y == 0:
        fid -= 1
        j -= 2
        y = int(line[j])
    else:
        #blocks += str(fid)
        res += fid * pos
        pos += 1
        x -=  1
        y -= 1

print(res)
#print(blocks)
