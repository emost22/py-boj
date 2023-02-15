import sys

while True:
    strList = sys.stdin.readline().split()
    x = strList[0].lower()
    if x == '#':
        break

    ret = 0
    for i in range(1, len(strList)):
        ret += strList[i].lower().count(x)
    print(x, ret)
