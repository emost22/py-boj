import re
import sys

r = re.compile('^[A-F]?A+F+C+[A-F]?$')
tc = int(sys.stdin.readline())
for t in range(tc):
    str = sys.stdin.readline().strip()
    if r.fullmatch(str):
        print('Infected!')
    else:
        print('Good')
