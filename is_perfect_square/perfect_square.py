import cmath
from decimal import Decimal, getcontext


def is_perfect_square(num, *, complex=False):
    if complex:
        root = cmath.sqrt(num)
        return _rounds_to_int(root.real) and _rounds_to_int(root.imag)
    else:
        if num < 0:
            return False
        getcontext().prec = 100
        root = Decimal(num).sqrt()
        return _rounds_to_int(root)


def _rounds_to_int(num):
    return int(num) == num
