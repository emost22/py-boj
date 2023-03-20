import sys

N = int(sys.stdin.readline())
arrList = [0 for i in range(0, N)]

for i in range(N):
    arrList[i] = int(sys.stdin.readline())
arrList.sort(reverse=True)

for i in range(N):
    print(arrList[i])
