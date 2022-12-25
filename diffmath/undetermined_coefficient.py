from typing import Union

from diffpy.equation.Equation import Equation
from diffpy.equation.Variable import Variable
from diffpy.derivative import differentiate
from diffpy.diffmath.homogeneous import homogeneous
from diffpy.equation.trigonometric import (Sin, Cos)
from diffpy.constants import e




x = Variable()

def undetermined_coefficient(a, b, c, eq:Equation):
    """

    """
    
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
    
    if eq.data['func'][0] == 'mul':
        return e_und_coeff(a, b, c, eq)





def x_und_coeff(a, b, c, eq, isMain=True, y=None, y1=None, y2=None):
    """

    """
    
    string, l = homogeneous(a, b, c)

    
    if y is None or y1 is None or y2 is None:
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

    if isMain:
        sign = '+'
        if A < 0:
            A *= -1
            sign = '-'
        return f"y = {string} {sign} {resA * x ** 2 + resB * x + resC}"
    return [resA, resB, resC]


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





def sin_cos__und_coeff (a, b, c, eq, isMain=True, y=None, y1=None, y2=None):
    """
    
    """

    string, l = homogeneous(a, b, c)

    n, b1 = get_sin(eq)
    m, b2 = get_cos(eq)
    i = b1

    if b1 != b2:
        raise Exception(f"I can't solve equation where sin and cos has different arguments: {eq}")
    
    if y is None or y1 is None or y2 is None:
        y = Sin(i * x) + Cos(i * x)
        y1 = differentiate(y)
        y2 = differentiate(y1)

    y *= c
    y1 *= b
    y2 *= a

    c = get_sin(y)[0] + get_sin(y2)[0]
    d = get_cos(y1)[0]
    e = get_sin(y1)[0]
    f = get_cos(y)[0] + get_cos(y2)[0]

    print(f"""y: {y}\ny': {y1}\ny": {y2}\nc: {c}\nd: {d}\ne: {e}\nf: {f}""")

    A = (m*e - n*f) / (e*d - f*c)
    B = (n - c*A) / e

    if isMain:
        sign = '+'
        if A < 0:
            A *= -1
            sign = '-'

        return f'y = {string} {sign} {A}sin({i}x) + {B}cos({i}x)'
    return [A, B]


def get_sin(eq):
    for el in eq.data['func'][1:]:
        if el.data['func'][0] == 'sin':
            if el.data['func'][1].data['pow'] != 1:
                raise Exception(f"I can't solve the equation where sin has comprehensive argument: {eq}")
            return [eq.data['const'] * el.data['const'], el.data['func'][1].data['const']]
    return [0, 0]

def get_cos(eq):
    for el in eq.data['func'][1:]:
        if el.data['func'][0] == 'cos':
            if el.data['func'][1].data['pow'] != 1:
                raise Exception(f"I can't solve the equation where cos has comprehensive argument: {eq}")
            return [eq.data['const'] * el.data['const'], el.data['func'][1].data['const']]
    return [0, 0]




def e_und_coeff(a, b, c, eq):
    """

    """

    string, l = homogeneous(a, b, c)
    e, type_x, equation, i = get_data_e(eq)

    if type_x:
        raise Exception(f"I can't solve this equation: {eq}")
    else:
        y = Sin(i * x) + Cos(i * x)
        y1 = (e - i) * Sin(i * x) + (e + i) * Cos(i * x)
        y2 = (e**2 - 2*e*i - i**2) * Sin(i * x) + (e**2 + 2*e*i - i**2) * Cos(i * x)

        print(f"""y: {y}\ny': {y1}\ny": {y2}\n\n""")


        A, B = sin_cos__und_coeff(a, b, c, equation, False, y, y1, y2)
        
        sign = '+'
        if A < 0:
            A *= -1
            sign = '-'

        return f'y = {string} {sign} ({A}sin({i}x) + {B}cos({i}x)) * e^({e}x)'


def get_data_e(eq):
    answer = None
    type_x = None
    equation = None
    i = None

    el : Equation
    for el in eq.data['func'][1:]:
        if int(el.data['const'] / e) == el.data['const'] / e and el.data['func'] == '':
            if not isinstance(differentiate(el.data['pow']), Union[int, float]):
                raise Exception(f"I can't solve the equation where power of e has comprehensive argument: {eq}")
            answer = differentiate(el.data['pow'])
            continue

        if el.data['func'][0] == 'sum' and equation is None:
            equation = el

        if el.data['func'][0] == 'sum' and el.data['func'][1].data['func']=='x' and type_x is None:
            type_x = True
        elif el.data['func'][0] == 'sum' and el.data['func'][1].data['func'][0] in ['sin','cos'] and type_x is None:
            type_x = False
            i = differentiate(el.data['func'][1].data['func'][1])
            if not isinstance(i, Union[int, float]):
                raise Exception(f"I can't solve the equation where cos has comprehensive argument: {eq}")
            
    if answer is None or type_x is None or equation is None:
        raise Exception(f"I can't solve this equation: {eq}")

    return [answer, type_x, equation, i]

