import sys

arrList = list(map(int, sys.stdin.readlines()))
for x in arrList:
    if x == 0:
        break

    while x >= 10:
        sum = 0
        y = x
        while y > 0:
            sum += (y % 10)
            y //= 10
        x = sum
    print(x)
