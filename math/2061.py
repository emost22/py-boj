import sys

K, L = map(int, sys.stdin.readline().split())

x = 0
for i in range(2, L):
    if K % i == 0:
        x = i
        break

if x > 0:
    print('BAD %d' % x)
else:
    print('GOOD')
