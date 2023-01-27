import sys

N = int(sys.stdin.readline())
arrList = list(map(int, sys.stdin.readline().split()))
arrList.sort(reverse=True)

ret = 0
for i in range(1, N):
    ret += (arrList[0] + arrList[i])
print(ret)
