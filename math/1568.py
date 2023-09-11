import sys

N = int(sys.stdin.readline())

r = 1
ret = 0
while N:
    if N < r:
        r = 1

    N -= r
    ret += 1
    r += 1

print(ret)
