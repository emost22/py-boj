dp = [0, 1]
for i in range(2, 91):
    dp.append(dp[i - 1] + dp[i - 2]);

x = int(input())
print(dp[x])
