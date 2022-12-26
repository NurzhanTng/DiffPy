from typing import Union

from diffpy.constants import (sin, cos, tan, cot, log, e)
from diffpy.equation.Equation import Equation
from diffpy.equation.Variable import Variable



def Sin(eq):
    """
    Function for creating the sin equation

    >>> from diffpy import (Sin, Variable)
    >>> eq = Sin(2 * x)
    """

    if isinstance(eq, Union[int, float]):
        return sin(eq)

    if isinstance(eq, Variable):
        eq = eq * 1

    return Equation(1, ['sin', eq], 1)


def Cos(eq):
    """
    Function for creating the sin equation

    >>> from diffpy import (Cos, Variable)
    >>> eq = Cos(2 * x)
    """

    if isinstance(eq, Union[int, float]):
        return cos(eq)

    if isinstance(eq, Variable):
        eq = eq * 1
    
    return Equation(1, ['cos', eq], 1)


def Tan(eq):
    """

    """

    if isinstance(eq, Union[int, float]):
        if cos(eq) == 0:
            return 0
        return tan(eq)

    if isinstance(eq, Variable):
        eq = eq * 1

    return Equation(1, ['tan', eq], 1)


def Cot(eq):
    """

    """
    
    if isinstance(eq, Union[int, float]):
        if sin(eq) == 0:
            return 0
        return cot(eq)
    
    if isinstance(eq, Variable):
        eq = eq * 1
    
    return Equation(1, ['cot', eq], 1)


def Log(eq, base=e):
    """

    """

    if isinstance(eq, Union[int, float]) and isinstance(base, Union[int, float]):
        return log(eq, base)

    if isinstance(eq, Variable):
        eq = eq * 1
    if base == 0:
        raise Exception("Wrong base for logarithm: 0")
        
    if int(base / e) == base / e:
        return Equation(1, ['ln', eq], 1)
    return Equation(1, ['log', eq, base], 1)