from vicky import calci
from my_cmd import command as c

from vicky import hello as h
import math, vicky

calci.add(4,5)

q, r = calci.div(8)
print('Quotient = {}'.format(q))
print('Remainder = {}'.format(r))

v = vicky.pie()
m = math.pi

if m == v:
    print()
    print(m, v)
else: print('unequal')

print('Hi, ' + h.hi())
h.bye('Ankit')

c.cmd()
