from typing import Union
from math import sin, cos
from diffpy.equation import Equation, x


def Sin(eq):
    if isinstance(eq, Union[int, float]):
        return sin(eq)

    if isinstance(eq, x):
        eq = eq * 1

    return Equation(1, ['sin', eq], 1)


def Cos(eq):
    if isinstance(eq, Union[int, float]):
        return cos(eq)

    if isinstance(eq, x):
        eq = eq * 1
    
    return Equation(1, ['cos', eq], 1)


def Tan(eq):
    if isinstance(eq, Union[int, float]):
        if cos(eq) == 0:
            return 0
        return sin(eq) / cos(x)

    if isinstance(eq, x):
        eq = eq * 1

    return Equation(1, ['tg', eq], 1)


def Cot(eq):
    if isinstance(eq, Union[int, float]):
        if sin(eq) == 0:
            return 0
        return cos(x) / sin(eq)
    
    if isinstance(eq, x):
        eq = eq * 1
    
    return Equation(1, ['ctg', eq], 1)