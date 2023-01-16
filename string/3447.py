import re
import sys

strList = sys.stdin.readlines()
for str in strList:
    while 'BUG' in str:
        str = re.sub('BUG', '', str)

    print(str, end='')
