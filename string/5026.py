import sys

N = int(sys.stdin.readline())
for i in range(0, N):
    str = sys.stdin.readline().strip()
    if str == 'P=NP':
        print('skipped')
    else:
        print(sum(list(map(int, str.split('+')))))
