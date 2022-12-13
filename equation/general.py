from __future__ import annotations
from typing import Union

class Equation():
    def __init__(self, const:int, func:Union[str, list[str, Equation]], power:Union[int, Equation]) -> None:
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

            elif self.data[pow] == 1 and  self.data['func'][0] == 'sum':
                for i in range(1, len(self.data['func'])):
                    if not isinstance(self.data['func'][i], Equation): continue
                    if self.data['func'][i].data['func'] == other.data['func'] and self.data['func'][i].data['pow'] == other.data['pow']:
                        self.data['func'][i].data['const'] += (other.data['const']) / self.data['const']
                        return self

                other.data['const'] /= self.data['const']
                self.data['func'].append(other)
                return self

            return Equation(1, ['sum', self, other], 1)
        
        raise Exception(f'Incorrect type of {other}: {type(other)}. It can be {int} or {self}')


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


    def __mul__(self, other:Union[int, Equation]):
        self.print_step('__mul__', other)

        if isinstance(other, int):
            self.data['const'] *= other
            return self

        if isinstance(other, Equation):
            if self.data['func'] == other.data['func']:
                self.data['const'] *= other.data['const']
                self.data['pow'] += other.data['pow']
                return self

            elif self.data['func'][0] == 'mul':
                for i in range(1, len(self.data['func'])):
                    if not isinstance(self.data['func'][i], Equation): continue

                    if self.data['func'][i].data['func'] == other.data['func']:
                        self.data['const'] *= other.data['const'] / self.data['const']
                        self.data['pow'] += other.data['pow'] / self.data['pow']
                        return self

                other.data['const'] /= self.data['const']
                self.data['func'].append(other)
                return self

            elif self.data[pow] == 1 and self.data['func'][0] == 'div':
                eq:Union[int, Equation] = self.data['func'][1].data

                if isinstance(eq['func'], list):
                    if eq['func'][0] == 'mul':
                        for i in range(1, len(self.data['func'])):
                            if not isinstance(self.data['func'][i], Equation): continue

                            if self.data['func'][i].data['func'] == other.data['func']:
                                self.data['const'] *= other.data['const'] / self.data['const']
                                self.data['pow'] += other.data['pow'] / self.data['pow']
                                return self
                                
                        other.data['const'] /= self.data['const']
                        other.data['pow'] /= self.data['pow']
                        eq['func'].append(other)
                        return self

            self.data['func'][1] = Equation(1, ['mul', self.data['func'][1], ], 1)
            return self

        raise Exception(f'Incorrect type of {other}: {type(other)}. It can be {int} or {self}')


    def __rmul__(self, other:Union[int, Equation]): 
        self.print_step('__rmul__', other)
        return self.__mul__(other)


    def __truediv__(self, other:Union[int, Equation]): NotImplemented
    

    def __rtruediv__(self, other:Union[int, Equation]): NotImplemented


    def __pow__(self, other:Union[int, Equation]): NotImplemented


    def __rpow__(self, other:Union[int, Equation]): NotImplemented


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


    def to_string(self):
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
                        string += f'({el.to_string()})'
                    else:
                        string += str(el)
                
        if power != 1:
            string = f'({string})^{power}'

        return string


    def print_step(self, func, other):
        if isinstance(other, Equation):
            print(f"{func}:\n   self: {self.to_string()}\n   other: {other.to_string()}\n")
        if isinstance(other, int):
            print(f"{func}:\n   self: {self.to_string()}\n   other: {other}\n")



def x()-> Equation: 
    '''
    Function for creating a variable x.
    It is forbidden to call 1 time and use several times.\n
    You need to write it as:
          from diffpy import x\n
          equation = x() + x()\n

    The following code will execute incorrectly:
          from diffpy import x\n
          equation = x + x, 
    or  
          import diffpy as df\n
          x = df.x()\n
          equation = x + x\n
    '''


    return Equation(1, 'x', 1)
