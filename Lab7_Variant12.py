k = int(input())
C = int(input())
a = []
for i in range(int(input())):
 a.append(int(input()))
a.append(0)
for i in range(len(a)-1, k, -1):
    a[i] = a[i - 1]
a[k] = C
print(a)
