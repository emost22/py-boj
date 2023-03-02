import re
import sys

tc = int(sys.stdin.readline())
r = re.compile('(100+1+|01)+')
for t in range(0, tc):
    x = sys.stdin.readline().strip()
    if r.fullmatch(x):
        print('YES')
    else:
        print('NO')
