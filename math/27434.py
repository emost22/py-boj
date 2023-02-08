import sys

N = int(sys.stdin.readline())
ret = 1
for i in range(2, N + 1):
    ret *= i
print(ret)
