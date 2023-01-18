import sys

N = int(sys.stdin.readline())
for i in range(0, N):
    strList = sys.stdin.readline().split()
    strList[0] = 'god'
    for str in strList:
        print(str, end='')
    print()
