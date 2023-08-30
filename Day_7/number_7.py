import random
n = 3
m = 3
matrix = [[random.randint(1, 12) for i in range(m)] for j in range(n)]
print(matrix)
for line in matrix:
    for column in line:
            print("%4d" % column, end=" ")
    print()
# print(matrix[0][0] + matrix[1][2] + matrix[2][2])
# print(matrix[0][2] + matrix[1][1] + matrix[2][0])
s = 0
for i in range(n):
    for j in range(m):
        if  i==j:
            s += matrix[i][j]
print(s)


