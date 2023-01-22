import sys


def isVowel(x):
    return x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'


while True:
    str = sys.stdin.readline().strip()
    if str == 'end':
        break

    if 'a' not in str and 'e' not in str and 'i' not in str and 'o' not in str and 'u' not in str:
        print('<' + str + '> is not acceptable.')
        continue

    aCnt = 0
    bCnt = 0
    if isVowel(str[0]):
        aCnt += 1
    else:
        bCnt += 1

    flag = True
    for i in range(1, len(str)):
        if str[i] == str[i - 1]:
            if str[i] != 'e' and str[i] != 'o':
                flag = False
                break
        if str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u':
            aCnt += 1
            bCnt = 0
        else:
            aCnt = 0
            bCnt += 1

        if aCnt == 3 or bCnt == 3:
            flag = False
            break

    if flag:
        print('<' + str + '> is acceptable.')
    else:
        print('<' + str + '> is not acceptable.')
