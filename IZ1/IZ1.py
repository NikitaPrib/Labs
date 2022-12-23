f = open('27-B.txt')
n = int(f.readline())
m = []
s = 0
for i in range(n):
    a = list(map(int, f.readline().split()))
    a.sort()
    m.append(a[1]-a[0])
    m.append(a[2]-a[0])
    s = s + a[1] + a[2]
if s % 4 == 0:
    print(s)
else:
    m.sort()
    j = 0
    while (s - m[j]) % 4 != 0:
        j += 1
    print(s - m[j])
