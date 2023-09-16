import sys

N = int(sys.stdin.readline())

ret = 6
for i in range(11, N + 1):
    ret *= i

print(ret)
