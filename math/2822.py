import sys

arrList = [
    (int(sys.stdin.readline()), 1),
    (int(sys.stdin.readline()), 2),
    (int(sys.stdin.readline()), 3),
    (int(sys.stdin.readline()), 4),
    (int(sys.stdin.readline()), 5),
    (int(sys.stdin.readline()), 6),
    (int(sys.stdin.readline()), 7),
    (int(sys.stdin.readline()), 8),
]

arrList.sort(reverse=True)

ret = []
sum = 0
for i in range(0, 5):
    sum += arrList[i][0]
    ret.append(arrList[i][1])

print(sum)
ret.sort()
for x in ret:
    print(x, end=' ')
