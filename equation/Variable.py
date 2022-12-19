from Equation import Equation
from typing import Union


class Variable(): 
    '''
    Class for creating a variable x
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
