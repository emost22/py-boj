import sys
from decimal import Decimal, getcontext

a, b, c = map(int, sys.stdin.readline().split())

getcontext().prec = 30
print("{:f}".format(Decimal(a) * Decimal(b) / Decimal(c)))
