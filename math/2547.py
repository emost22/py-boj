import sys

tc = int(sys.stdin.readline())
for t in range(tc):
    sys.stdin.readline()
    N = int(sys.stdin.readline())

    sum = 0
    for i in range(N):
        sum += int(sys.stdin.readline())
    if sum % N == 0:
        print('YES')
    else:
        print('NO')
