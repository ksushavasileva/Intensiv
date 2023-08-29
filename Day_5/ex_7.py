n = int(input("введите число n>=2 "))
a = []
d = []
for i in range(n):
    a.append(int(input()))
for i in range(n-1):
    d.append(a[i] + a[i + 1])



print(a)
print(d)
