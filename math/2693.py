import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    arrList = list(map(int, sys.stdin.readline().split()))
    arrList.sort(reverse=True)
    print(arrList[2])
