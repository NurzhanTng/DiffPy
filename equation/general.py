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
        self.print_step('__add__', other)

        if isinstance(other, int):
            return Equation(1, ['sum', self, other], 1)

        if isinstance(other, Equation):
            if self.data['func'] == other.data['func']:
                self.data['const'] += other.data['const']
                return self

            elif self.data['func'][0] == 'sum':
                for i in range(1, len(self.data['func'])):
                    if not isinstance(self.data['func'][i], Equation):
                        print(self.data['func'][i], other.data['func'])
                        continue
                    if self.data['func'][i].data['func'] == other.data['func']:
                        self.data['func'][i].data['const'] += other.data['const']
                        return self

                self.data['func'].append(other)
                return self

            return Equation(1, ['sum', self, other], 1)


    def __radd__(self, other:Union[int, Equation]):
        self.print_step('__radd__', other)
        return self.__add__(other)


    def __sub__(self, other:Union[int, Equation]):
        self.print_step('__sub__', other)
        if isinstance(other, Equation):
            other.data['const'] *= -1
        elif isinstance(other, int):
            other *= -1
        
        return self.__add__(other)


    def __rsub__(self, other:Union[int, Equation]):
        self.print_step('__rsub__', other)
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
        string = str(const) + '*' if const != 1 else ''

        if func == 'x':
            string += f'x'
        elif isinstance(func, list):
            if func[0] == 'sum':
                for i in range(1, len(func)):
                    el = func[i]
                    if i > 1:
                        string += ' + '

                    if isinstance(el, Equation):
                        string += f'({el.show_equation()})'
                    else:
                        string += str(el)
                
        if power != 1:
            string = f'({string})^{power}'

        return string


    def print_step(self, func, other):
        if isinstance(other, Equation):
            print(f"{func}:\n   self: {self.show_equation()}\n   other: {other.show_equation()}\n")
        if isinstance(other, int):
            print(f"{func}:\n   self: {self.show_equation()}\n   other: {other}\n")



def x()-> Equation: 
    return Equation(1, 'x', 1)
