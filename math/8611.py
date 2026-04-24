import sys

N = int(sys.stdin.readline())


def base(n, i):
    ret = ''

    while n > 0:
        n, mod = divmod(n, i)
        ret += str(mod)

    return ret


chk = False
for i in range(2, 11):
    x = base(N, i)

    l = 0
    r = len(x) - 1
    flag = True
    while l < r:
        if x[l] != x[r]:
            flag = False
            break
        l += 1
        r -= 1

    if flag:
        chk = True
        print(i, x)

if not chk:
    print('NIE')
