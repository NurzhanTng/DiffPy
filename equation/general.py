from __future__ import annotations
from typing import Union

class Equation():
    def __init__(self, const, func, power) -> None:
        self.data = {
            'const': const, 
            'func': func, 
            'pow': power
        }


    def __add__(self, other:Union[int, Equation]):
        if isinstance(other, int):
            return Equation(1, ['sum', self, other], 1)

        if isinstance(other, Equation):
            if self.data['func'] == other.data['func']:
                self.data['const'] += other.data['const']
                return self
            return Equation(1, ['sum', self, other], 1)


    def __radd__(self, other:Union[int, Equation]):
        return self.__add__(other)


    def __sub__(self, other:Union[int, Equation]):
        if isinstance(other, Equation):
            other.data['const'] *= -1
        if isinstance(other, int):
            other *= -1
        
        return self.__add__(other)


    def __rsub__(self, other:Union[int, Equation]):
        self.data['const'] *= -1
        return self.__add__(other)


    def __mul__(self, other:Equation):
        if type(other) == type(self):
            return Equation(self.data * other.data)
        if type(other) == type(1):
            return Equation(self.data * other)
        raise Exception(f'Incorrect type of {other}: {type(other)}. It can be {int} or {self}')


    def __rmul__(self, other):
        return self.__mul__(other)


    def __truediv__(self, other:Equation):
        if type(other) == type(self):
            return Equation(self.data / other.data)
        if type(other) == type(1):
            return Equation(self.data / other)
        raise Exception(f'Incorrect type of {other}: {type(other)}. It can be {int} or {self}')
    

    def __rtruediv__(self, other):
        return self.__truediv__(other)


    def show_data(self, func=None):
        def tabs(tab):
            return ' ' * (tab * 2)
        
        def return_list(l:list, tab):
            string = ''
            for el in l:
                if isinstance(el, Equation):
                    string += return_equation(el, tab + 1) + ',\n'
                elif isinstance(el, int):
                    string += tabs(tab + 1) + f'{el},\n'
                else:
                    string += tabs(tab + 1) + f'"{el}",\n'
            return tabs(tab) + '[\n' + string + tabs(tab) + ']\n'

        def return_equation(eq:Equation, tab):
            string = ''
            for key in eq.data.keys():
                data = eq.data[key]
                if isinstance(data, list):
                    string += return_list(data, tab + 1)
                elif isinstance(data, Equation):
                    string += return_equation(data, tab + 1) + '\n'
                else:
                    string += tabs(tab + 1) + f'{key}: {data},\n'
            return tabs(tab) + '{\n' + string + tabs(tab) + '}'

        
        string = return_equation(self, 0)
        print(string)


    def show_equation(self):
        const, func, power = self.data.values()
        string = str(const) + '*'

        if func == 'x':
            string += f'x'
        elif isinstance(func, list):
            string += '('
            if func[0] == 'sum':
                for i in range(1, len(func)):
                    el = func[i]
                    if i > 1:
                        string += ' + '

                    if isinstance(el, Equation):
                        string += f' {el.show_equation()} '
                    else:
                        string += str(el)
                    
            string += ')'

        string += f'^{power}'

        return string


def x()-> Equation: 
    return Equation(1, 'x', 1)
