import random
n = 3
m = 3
matrix = [[random.randint(1, 12) for o in range(m)] for k in range(n)]
print(matrix)
for line in matrix:
    for column in line:
            print("%4d" % column, end=" ")
    print()

for i in range(n):
    matrix[i].pop(-1)
    s = sum(matrix[i])
    matrix[i].append(s)
print(matrix)