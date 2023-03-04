import sys

N = int(sys.stdin.readline())
arrList = list(map(int, sys.stdin.readline().split()))
maxScore = arrList[0]
minScore = arrList[0]
for i in range(1, N):
    maxScore = max(maxScore, arrList[i])
    minScore = min(minScore, arrList[i])
print(maxScore - minScore)
