import sys

for t in range(3):
    N = int(sys.stdin.readline())
    ret = 0
    for i in range(N):
        ret += int(sys.stdin.readline())

    if ret == 0:
        print(0)
    elif ret > 0:
        print('+')
    else:
        print('-')
