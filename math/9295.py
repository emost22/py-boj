import sys

N = int(sys.stdin.readline())
for i in range(1, N + 1):
    x, y = map(int, sys.stdin.readline().split())
    print('Case %d: %d' % (i, x + y))
