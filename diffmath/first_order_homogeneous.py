from diffpy.integral.integrate import integrate
from diffpy.diffmath.first_order import _isLn
from diffpy.constants import e


def first_order_homogeneous(a, b):
    """
    A function created to solve equations of type `f(x)*y' + p(x)*y = 0`
    ==================================================================

    Formulas:

    a*y' + b*y = 0

    a*(dy/dx) + b*y = 0

    dy/dx = (-b/a)*y

    dy/y = (-b/a)dx

    ln|y| = (-b/a)*x + C

    e^(ln|y|) = e^((-b/a)*x + C)

    y = C*e^((-b/a)*x)
    """

    right_eq = integrate(-1*b * a**(-1))

    if _isLn(right_eq):
        y = right_eq.data['func'][1]
    else:
        y = e**(right_eq)

    return f'y = C * {y}'
