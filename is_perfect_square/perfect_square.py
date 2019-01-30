import cmath
from decimal import Context, Decimal, getcontext, localcontext


def is_perfect_square(num, *, complex=False):
    if complex:
        root = cmath.sqrt(num)
        return _is_integer(root.real) and _is_integer(root.imag)
    else:
        if num < 0:
            return False
        digit_count = len(str(num))
        with localcontext(Context(prec=digit_count * 2)):
            root = Decimal(num).sqrt()
        return _is_integer(root)


def _is_integer(num):
    return int(num) == num
