d = {}
for i in range(int(input())):
    for j in input().split():
        d[j] = d.get(j,0)+1

print(sorted(d.items(), key = lambda x:x[1]), "\n")
a = []
for j in d:
    a.append((100-d[j],j))
[print(b[1]) for b in sorted(a)]
