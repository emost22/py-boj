import sys

dp = [0, 1]
N = int(sys.stdin.readline())
for i in range(2, N + 1):
    dp.append(dp[i - 1] + dp[i - 2])
print(dp[N])
