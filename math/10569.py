import sys

tc = int(sys.stdin.readline())

for t in range(tc):
    x, y = map(int, sys.stdin.readline().split())
    print(y - x + 2)
