import sys
from collections import deque

dq = deque([])
N = int(sys.stdin.readline())
for i in range(N):
    btn = sys.stdin.readline().split()
    if btn[0] == '1':
        dq.append([btn[1], i])
    elif btn[0] == '2':
        dq.appendleft([btn[1], i])
    else:
        if len(dq) == 0:
            continue

        if dq[0][1] < dq[-1][1]:
            dq.pop()
        else:
            dq.popleft()

if len(dq) == 0:
    print(0)
else:
    for x in dq:
        print(x[0], end='')
    print()
