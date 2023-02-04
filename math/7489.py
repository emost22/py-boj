import sys

tc = int(sys.stdin.readline())

for t in range(tc):
    N = int(sys.stdin.readline())

    ret = 1
    for i in range(2, N + 1):
        ret *= i

    while ret % 10 == 0:
        ret //= 10
    print(ret % 10)
