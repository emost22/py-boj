import sys


def func():
    stack = []
    str = sys.stdin.readline().strip()
    for x in str:
        if x == '(':
            stack.append(x)
        else:
            if len(stack) == 0:
                return 'NO'
            else:
                stack.pop()

    if len(stack) != 0:
        return 'NO'
    else:
        return 'YES'


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    for t in range(0, N):
        print(func())
