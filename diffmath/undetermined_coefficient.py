from typing import Union

from diffpy.equation.Equation import Equation
from diffpy.equation.Variable import Variable
from diffpy.derivative import differentiate
from diffpy.diffmath.homogeneous import homogeneous




x = Variable()

def undetermined_coefficient(a, b, c, eq:Equation):
    if eq.data['func'] == '':
        return
        
    if eq.data['func'][0]=="sum":
        res = Exception(f"I can't solve this equation: {eq}")

        if eq.data['func'][1].data['func']=='x':
            res=x_und_coeff(a, b, c, eq)
        if eq.data['func'][1].data['func'][0] in ['sin','cos']:
            res=sin_cos__und_coeff(a, b, c, eq)

        if isinstance(res, Exception):
            raise res
        return res
    
    # if eq.data['func'][0] == 'mul':
    #     return e_und_coeff(l, q)





def x_und_coeff(a, b, c, eq):
    string, l = homogeneous(a, b, c)

    y=1 + x + x**2 
    y1=differentiate(y)
    y2=differentiate(y1)

    y *= c
    y1 *= b
    y2 *= a

    A = _get_x_pow2(y) * x**2 + _get_x_pow1(y1) * x + _get_x_pow0(y2)
    B = (_get_x_pow1(y) * x + _get_x_pow0(y1)) 
    C = _get_x_pow0(y)

    i = _get_x_pow2(eq)
    j = _get_x_pow1(eq)
    k = _get_x_pow0(eq)

    resA = i / _get_x_pow2(A)
    resB = (j - resA * _get_x_pow1(A)) / _get_x_pow1(B)
    resC = (k  - resA * _get_x_pow0(A) - resB * _get_x_pow0(C)) / _get_x_pow0(B)

    return f"y = {string} + {resA * x ** 2 + resB * x + resC}"


def _get_x_pow2(eq):
    for el in eq.data['func'][1:]:
        if isinstance(el, Union[int, float]):
            continue
        if el.data['pow'] == 2:
            return el.data['const'] * eq.data['const']
    return 0

def _get_x_pow1(eq):
    for el in eq.data['func'][1:]:
        if isinstance(el, Union[int, float]):
            continue
        if el.data['pow'] == 1:
            return el.data['const'] * eq.data['const']
    return 0

def _get_x_pow0(eq):
    if isinstance(eq, Union[int, float]):
        return eq
    for el in eq.data['func'][1:]:
        if isinstance(el, Union[float, int]):
            return el * eq.data['const']
    return 0





def sin_cos__und_coeff (a, b, c, eq):
    string, l = homogeneous(a, b, c)

    n, b1 = get_sin(eq)
    m, b2 = get_cos(eq)

    i = b2

    step1 = n*i
    step2 = (c - a*i**2)
    step3 = (step1 + m * step2)
    step4 = b*i
    step5 = (step4**2) - (step2**2)

    A = step3 / (step5)
    B = (m - A*step2) / step4

    return f'y = {string} + {A}sin({i}x) + {B}cos({i}x)'

def get_sin(eq):
    for el in eq.data['func'][1:]:
        if el.data['func'][0] == 'sin':
            return [eq.data['const'] * el.data['const'], el.data['func'][1].data['const']]
    return [0, 0]

def get_cos(eq):
    for el in eq.data['func'][1:]:
        if el.data['func'][0] == 'cos':
            return [eq.data['const'] * el.data['const'], el.data['func'][1].data['const']]
    return [0, 0]