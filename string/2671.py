import re
import sys

str = sys.stdin.readline().strip()
r = re.compile('(100+1+|01)+')

if r.fullmatch(str):
    print('SUBMARINE')
else:
    print('NOISE')
