import sys

dp = [0 for i in range(0, 1001)]

dp[2] = 1
N = int(sys.stdin.readline())
for i in range(3, N + 1):
    dp[i] = dp[i - 1] * 2
    if i % 2 == 0:
        dp[i] += 1
    else:
        dp[i] -= 1
print(dp[N])
