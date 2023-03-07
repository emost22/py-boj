import sys

arrList = []
N, K = map(int, sys.stdin.readline().split())
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        arrList.append(i)
        if i != N // i:
            arrList.append(N // i)
arrList.sort()
if K > len(arrList):
    print(0)
else:
    print(arrList[K - 1])
