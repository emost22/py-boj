import sys

N = int(sys.stdin.readline())
for t in range(N):
    alpha = [False for i in range(0, 26)]
    str = sys.stdin.readline().strip().replace(' ', '').lower()

    for ch in str:
        if 'a' <= ch <= 'z':
            alpha[ord(ch) - 97] = True

    ret = []
    for i in range(26):
        if not alpha[i]:
            ret.append(chr(i + 97))

    if len(ret) == 0:
        print('pangram')
    else:
        print('missing ', end='')
        for x in ret:
            print(x, end='')
        print()
