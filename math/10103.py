import sys

N = int(sys.stdin.readline())

s1 = 100
s2 = 100
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    if x < y:
        s1 -= y
    elif x > y:
        s2 -= x
print(s1)
print(s2)
