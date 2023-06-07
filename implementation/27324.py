import sys

x = int(sys.stdin.readline())
if x // 10 == x % 10:
    print(1)
else:
    print(0)
