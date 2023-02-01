import sys

stack = []
ret = 0

N = int(sys.stdin.readline())
for i in range(N):
    work = list(map(int, sys.stdin.readline().split()))
    if work[0] == 1:
        stack.append([work[1], work[2]])

    if len(stack) > 0:
        stack[-1][1] -= 1
        if stack[-1][1] == 0:
            ret += stack[-1][0]
            stack.pop()
print(ret)
