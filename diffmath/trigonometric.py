from typing import Union

from diffpy.equation import Equation

class Sin():
    def __init__(self, eq:Union[int, Equation]) -> None:
        self.data = Equation(1, ['sin', eq], 1)

    def print_data(self):
        print(self.data)