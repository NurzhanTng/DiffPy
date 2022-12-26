from diffpy.integral.integrate import integrate
from diffpy.diffmath.first_order import _isLn
from diffpy.constants import e


def first_order_homogeneous(a, b):
    right_eq = integrate(-1*b * a**(-1))

    if _isLn(right_eq):
        y = right_eq.data['func'][1]
    else:
        y = e**(right_eq)

    return f'y = {y} + C'

