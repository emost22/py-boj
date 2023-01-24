import sys

N = int(sys.stdin.readline())
arrList = list(map(int, sys.stdin.readline().split()))

ret = 0
cnt = 0
for x in arrList:
    if x == 1:
        cnt += 1
        ret += cnt
    else:
        cnt = 0
print(ret)
