import sys

N, M = map(int, sys.stdin.readline().split())
N = N + 1
dp = [[0 for i in range(N)] for i in range(N)]
for i in range(1, N):
    dp[i] = list(map(int, ("0 " + sys.stdin.readline()).split()))

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] += (dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1])

for i in range(0, M):
    sx, sy, ex, ey = map(int, sys.stdin.readline().split())
    print(dp[ex][ey] - dp[ex][sy - 1] - dp[sx - 1][ey] + dp[sx - 1][sy - 1])
