import random
n = 3
m = 4
matrix = [[random.randint(1, 12) for i in range(m)] for j in range(n)]
print(matrix)
print("введи диапазон")
a = int(input())
b = int(input())
c = 0
for line in matrix:
    for column in line:
        if (column >= a) and (column <= b):
            c += 1

print(c)