from typing import Union

from diffpy.constants import (sin, cos, tan, cot, log)
from diffpy.equation.Equation import Equation
from diffpy.equation.Variable import Variable



def Sin(eq):
    """

    """

    if isinstance(eq, Union[int, float]):
        return sin(eq)

    if isinstance(eq, Variable):
        eq = eq * 1

    return Equation(1, ['sin', eq], 1)



def Cos(eq):
    """

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