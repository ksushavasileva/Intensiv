n = int(input())
a = []
b = []
for i in range(n):
    s = int(input())
    a.append(s)
print(a)
for c in range(a):
    if c < 0:
        b.append(-1)
    elif c > 0:
        b.append(1)
    else: b.append(i)
print(b)

