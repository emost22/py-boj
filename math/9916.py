import sys

N = int(sys.stdin.readline())

ret = 1
for i in range(1, N + 1):
    ret *= i

ans = 0
while ret:
    if ret % 10 == 0:
        ans += 1
    ret //= 10
print(ans)
