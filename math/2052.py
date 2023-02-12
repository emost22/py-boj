import sys

N = int(sys.stdin.readline())
ret = str(format(2 ** (-N), '.250f'))

while True:
    idx = len(ret) - 1
    if ret[idx] == '0':
        ret = ret[:idx] + ret[idx + 1:]
    else:
        break
print(ret)
