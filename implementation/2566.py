import sys

N = 9
arrList = [[0 for i in range(N)] for i in range(N)]

for i in range(N):
    arrList[i] = list(map(int, sys.stdin.readline().split(' ')))

x = 0
y = 0
maxValue = -1
for i in range(N):
    for j in range(N):
        if maxValue < arrList[i][j]:
            maxValue = arrList[i][j]
            x = i + 1
            y = j + 1

print(maxValue)
print(x, y)
