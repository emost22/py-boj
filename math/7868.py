import sys

MAX = 10 ** 18
LOG = 60

p1, p2, p3, N = map(int, sys.stdin.readline().split())

list = []

for i in range(0, LOG):
    if p1 ** i > MAX: break
    for j in range(0, LOG):
        if p1 ** i * p2 ** j > MAX: break
        for k in range(0, LOG):
            if p1 ** i * p2 ** j * p3 ** k > MAX: break
            list.append(p1 ** i * p2 ** j * p3 ** k)

list.sort()
print(list[N])
