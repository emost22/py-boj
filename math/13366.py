import sys

tc = int(sys.stdin.readline())
for t in range(tc):
    x = int(sys.stdin.readline())

    if x % 9 == 0:
        print('YES')
    else:
        print('NO')
