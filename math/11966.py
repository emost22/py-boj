import sys

arrList = [0 for i in range(0, 31)]

for i in range(0, 31):
    arrList[i] = (1 << i)

N = int(sys.stdin.readline())
if N in arrList:
    print(1)
else:
    print(0)
