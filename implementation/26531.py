import sys

arrList = sys.stdin.readline().split()
x = int(arrList[0])
y = int(arrList[2])
z = int(arrList[4])

if x + y == z:
    print("YES")
else:
    print("NO")
