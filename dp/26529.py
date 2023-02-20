import sys

N = 45
dp = [1, 1]
for i in range(2, N + 1):
    dp.append(dp[i - 1] + dp[i - 2]);

tc = int(sys.stdin.readline())
for t in range(tc):
    x = int(sys.stdin.readline())
    print(dp[x])
