import sys

l, r = map(int, sys.stdin.readline().split())
if l > r:
    l, r = r, l

print(r * (r + 1) // 2 - l * (l - 1) // 2)
