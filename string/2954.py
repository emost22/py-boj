import sys

strList = sys.stdin.readline().split()

for str in strList:
    ret = ''
    idx = 0
    while idx < len(str):
        ret += str[idx]
        if str[idx] == 'a' or str[idx] == 'e' or str[idx] == 'i' or str[idx] == 'o' or str[idx] == 'u':
            idx += 3
            continue
        else:
            idx += 1
    print(ret, end=' ')
