import sys

N = int(sys.stdin.readline())
arrList = list(map(int, sys.stdin.readline().split()))

ret = 0
maxValue = 0
for i in range(N - 1, -1, -1):
    maxValue = max(maxValue, arrList[i])
    ret = max(ret, maxValue - arrList[i])
print(ret)
