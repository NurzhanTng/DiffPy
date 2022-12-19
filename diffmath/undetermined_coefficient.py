from diffpy.diffmath.homogeneous import homogeneous
from diffpy.equation.Equation import Equation
from diffpy.equation.Variable import Variable
from diffpy.derivative import differentiate


x = Variable()

def undetermined_coefficient(a, b, c, eq:Equation):
    string, equations = homogeneous(a,b,c)

    if eq.data['func'][0]=="sum":
        if eq.data['func'][1].data['func']=='x':
            res = x_und_coeff(a, b, c, eq)
        # if eq.data['func'][1].data['func'] in ['sin','cos']:
        #     res = sin_und_coeff(eq)
        return res
    
    # if eq.data['func'][0] == 'mul':
    #     return e_und_coeff(l, q)


def x_und_coeff(a, b, c, eq):
    y = 1 + x + x**2
    y1 = differentiate(y)
    y2 = differentiate(y1)

    y *= a
    y1 *= b
    y2 *= c

    A = _get_x_pow2(y) * x**2 + _get_x_pow1(y1) * x + _get_x_pow0(y2)
    B = (_get_x_pow1(y) * x + _get_x_pow0(y1)) 
    C = _get_x_pow0(y2)

    i = _get_x_pow2(eq)
    j = _get_x_pow1(eq)
    k = _get_x_pow0(eq)

    resA = i / _get_x_pow2(A)
    resB = (j - resA * _get_x_pow1(A)) / _get_x_pow1(B)
    resC = (k  - resA * _get_x_pow1(A) - resB * _get_x_pow0(C)) / _get_x_pow1(B)

    return resA * x ** 2 + resB * x + resC


def _get_x_pow2(eq):
    for el in eq.data['func'][1:]:
        if el.data['pow'] == 2:
            return el.data['const']

def _get_x_pow1(eq):
    for el in eq.data['func'][1:]:
        if el.data['pow'] == 1:
            return el.data['const']

def _get_x_pow0(eq):
    for el in eq.data['func'][1:]:
        if isinstance(el, int):
            return el
