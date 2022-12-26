from __future__ import annotations
from typing import Union

from diffpy.equation.Equation import Equation


class Variable(): 
    r'''
    Class for creating a variable x
    ===============================
    
    Example of using Variable:
    
    >>> from diffpy import Variable
    >>> x = Variable()
    <class Variable>
    >>> eq = 5*x + 10
    <class Equation>
    '''

    def __init__(self) -> None:
        self.data = {
            'const': 1, 
            'func': 'x', 
            'pow': 1
        }

    def __add__(self, other:Union[int, Equation]):
        return Equation(1, 'x', 1) + other

    def __radd__(self, other:Union[int, Equation]):
        return other + Equation(1, 'x', 1)

    def __sub__(self, other:Union[int, Equation]):
        return Equation(1, 'x', 1) - other

    def __rsub__(self, other:Union[int, Equation]):
        return other - Equation(1, 'x', 1)

    def __mul__(self, other:Union[int, Equation]):
        return Equation(1, 'x', 1) * other

    def __rmul__(self, other:Union[int, Equation]): 
        return other * Equation(1, 'x', 1)

    def __truediv__(self, other:Union[int, Equation]):
        return Equation(1, 'x', 1) / other

    def __rtruediv__(self, other:Union[int, Equation]):
        return other / Equation(1, 'x', 1)

    def __pow__(self, other:Union[int, Equation]):
        return Equation(1, 'x', 1) ** other

    def __rpow__(self, other:Union[int, Equation]):
        return other ** Equation(1, 'x', 1) 
