import sys

arrList = [
    int(sys.stdin.readline()),
    int(sys.stdin.readline()),
    int(sys.stdin.readline()),
    int(sys.stdin.readline()),
    int(sys.stdin.readline())
]

arrList.sort()
print(sum(arrList) // 5)
print(arrList[2])
