import sys

N, K = map(int, sys.stdin.readline().split())
list = [0 for i in range(N)]
for i in range(0, N):
    list[i] = int(sys.stdin.readline())

list.sort(reverse=True)

ret = 0
for i in range(0, K):
    ret += list[i]
print(ret)
