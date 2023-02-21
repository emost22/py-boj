import sys

N = int(sys.stdin.readline())
for t in range(1, N + 1):
    url = sys.stdin.readline().strip()

    protocol = url.split("://")[0]
    div = url[url.find("://") + 3:]

    idx1 = -1
    idx2 = -1
    for i in range(len(div)):
        if div[i] == ':' and idx1 == -1 and idx2 == -1:
            idx1 = i
        if div[i] == '/' and idx2 == -1:
            idx2 = i

    print('URL #%d' % t)
    print('Protocol = %s' % protocol)
    if idx1 == -1 and idx2 == -1:
        print('Host     = %s' % div)
        print('Port     = <default>')
        print('Path     = <default>')
    elif idx1 == -1:
        print('Host     = %s' % div[:idx2])
        print('Port     = <default>')
        print('Path     = %s' % div[idx2 + 1:])
    elif idx2 == -1:
        print('Host     = %s' % div[:idx1])
        print('Port     = %s' % div[idx1 + 1:])
        print('Path     = <default>')
    else:
        print('Host     = %s' % div[:idx1])
        print('Port     = %s' % div[idx1 + 1:idx2])
        print('Path     = %s' % div[idx2 + 1:])
    if t < N:
        print()
