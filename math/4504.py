import sys

N = int(sys.stdin.readline())

while True:
    x = int(sys.stdin.readline())
    if x == 0:
        break

    if x % N == 0:
        print('%s is a multiple of %s.' % (x, N))
    else:
        print('%s is NOT a multiple of %s.' % (x, N))
