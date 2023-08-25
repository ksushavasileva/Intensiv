M = int(input())
N = int(input())
for i in range(M, N+1):
    flag = i % 3
    if flag ==0:
        print(i)
        