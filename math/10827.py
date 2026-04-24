import sys
from decimal import Decimal, getcontext

a, b = sys.stdin.readline().split()

getcontext().prec = 1200
print("{:f}".format(Decimal(a) ** Decimal(b)))
