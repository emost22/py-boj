import sys

while True:
    chk = [False for i in range(0, 26)]
    str = sys.stdin.readline().strip().replace(" ", "")
    if str == '*':
        break

    cnt = 0
    for x in str:
        if not chk[ord(x) - 97]:
            cnt += 1
        chk[ord(x) - 97] = True

    if cnt == 26:
        print("Y")
    else:
        print("N")
