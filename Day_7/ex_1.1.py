import random
n = 3
m = 4
matrix = [[random.randint(1, 12) for i in range(m)] for j in range(n)]
print(matrix)
for line in matrix:
    print(" ".join(map(str,line)))