import sys

while True:
    str = sys.stdin.readline().strip().replace(' ', '').lower()
    if str == '#':
        break
    
    alpha = [False for i in range(0, 26)]

    ret = 0
    for x in str:
        if 'a' <= x <= 'z':
            if alpha[ord(x) - 97]:
                continue
            else:
                ret += 1
                alpha[ord(x) - 97] = True

    print(ret)
