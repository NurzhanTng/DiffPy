from __future__ import annotations
from typing import Union

from diffpy.constants import e


class Equation():
    def __init__(self, const:int, func:Union[str, list[str, Equation]], power:Union[int, Equation]) -> None:
        self.data = {
            'const': const, 
            'func': func, 
            'pow': power
        }


    def __add__(self, other:Union[int, float, Equation]):
        self.print_step('__add__', other)
        other = other * 1

        if isinstance(other, Union[int, float]):
            if self.data['pow'] == 1 and  self.data['func'][0] == 'sum':
                self.data['func'].append(other / self.data['const'])
                return self
            return Equation(1, ['sum', self, other], 1)

        if isinstance(other, Equation):
            if self.data['func'] == other.data['func'] and self.data['pow'] == other.data['pow']:
                self.data['const'] += other.data['const']
                return self

            condit1 = self.data['pow'] == 1 and  self.data['func'][0] == 'sum'
            condit2 = other.data['pow'] == 1 and  other.data['func'][0] == 'sum'

            def append_to_sum(eq1:Equation, eq2:Union[int, float, Equation]):
                func = eq1.data['func']
                for i in range(1, len(eq1.data['func'])):
                    if type(eq2) != type(func[i]): continue
                    if isinstance(func[i], Union[int, float]) and isinstance(eq2, Union[int, float]):
                        func[i] += eq2
                        return eq1
                    if not isinstance(eq2, Equation): continue
                    if func[i].data['func'] == eq2.data['func'] and func[i].data['pow'] == eq2.data['pow']:
                        func[i].data['const'] += (eq2.data['const']) / eq1.data['const']
                        return eq1

                eq2.data['const'] /= eq1.data['const']
                eq1.data['func'].append(eq2)
                return eq1
                
            if condit1 and not condit2:
                return append_to_sum(self, other)
            elif condit2 and not condit1:
                return append_to_sum(other, self)
            elif condit1 and condit2:
                for eq in other.data['func'][1:]:
                    self = append_to_sum(self, eq)
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
        other = other * 1

        if isinstance(other, Union[int, float]):
            self.data['const'] *= other
            return self

        if isinstance(other, Equation):
            if self.data['func'] == other.data['func']:
                self.data['const'] *= other.data['const']
                self.data['pow'] += other.data['pow']

                if self.data['pow'] == 0:
                    return self.data['const']

                return self

            elif self.data['func'] == '':
                ...

            elif self.data['func'][0] == 'mul':
                for i in range(1, len(self.data['func'])):
                    if not isinstance(self.data['func'][i], Equation): continue

                    el:Equation = self.data['func'][i]
                    is_func_equal = el.data['func'] == other.data['func']
                    is_const_equal = el.data['const'] == other.data['const']

                    if (is_func_equal and other.data['func'] == '') and is_const_equal:
                        el.data['pow'] = el.data['pow'] + other.data['pow']
                        return self
                    elif is_func_equal:
                        el.data['const'] *= other.data['const'] / self.data['const']
                        el.data['pow'] += other.data['pow'] / self.data['pow']
                        return self

                other.data['const'] /= self.data['const']
                self.data['func'].append(other)
                return self

            return Equation(1, ['mul', self, other], 1)

        raise Exception(f'Incorrect type of {other}: {type(other)}. It can be {int} or {self}')


    def __rmul__(self, other:Union[int, Equation]): 
        self.print_step('__rmul__', other)
        return self.__mul__(other)


    def __truediv__(self, other:Union[int, Equation]):
        self.print_step('__div__', other)
        if isinstance(other, Equation):
            other.data['pow'] *= -1
            if other.data['func'] != '':
                other.data['const'] = 1 / other.data['const']
        else:
            other = 1 / other
        return self.__mul__(other)
    

    def __rtruediv__(self, other:Union[int, Equation]):
        self.print_step('__rdiv__', other)
        self.data['pow'] *= -1
        other.data['const'] = 1 / other.data['const']
        return self.__mul__(other)


    def __pow__(self, other:Union[int, Equation]):
        self.print_step('__pow__', other)
        self.data['pow'] = other * self.data['pow']
        return self


    def __rpow__(self, other:Union[int, Equation]):
        self.print_step('__rpow_', other)
        if isinstance(other, Equation):
            other.data['pow'] = self * other.data['pow']
            return other
        return Equation(other, '', self)


    def __str__(self):
        const, func, power = self.data.values()
        
        string = ''
        if int(const / e) == const / e:
            string += f'{int(const / e) if int(const / e) != 1 else ""}e{"" if func == "" else "*"}'
        elif const != 1:
            string += str(const) + '*'

        if func == 'x':
            string += 'x'
        elif isinstance(func, list):
            if func[0] in ['sin', 'cos', 'tan', 'cot']:
                string += f"{func[0]}{str(func[1])}"

            elif func[0] == 'sum':
                string += '('
                for i in range(1, len(func)):
                    el = func[i]
                    if i > 1:
                        string += ' + '
                    string += str(el)
                string += ')'

            elif func[0] == 'mul':
                for i in range(1, len(func)):
                    el = func[i]
                    if i > 1:
                        string += ' * '

                    string += str(el)
            
        if isinstance(power, Union[int, float]) and power != 1:
            string = f'{string}^{power}'
        elif isinstance(power, Equation):
            string = f'{string}^({power})'

        return string[:len(string)]


    def show_data(self, func=None):
        def tabs(tab):
            return ' ' * (tab * 2)
        
        def return_list(l:list, tab):
            string = ''
            for el in l:
                if isinstance(el, Equation):
                    string += return_equation(el, tab + 1) + ',\n'
                elif isinstance(el, Union[int, float]):
                    string += tabs(tab + 1) + f'{el},\n'
                else:
                    string += tabs(tab + 1) + f'"{el}",\n'
            return '[\n' + string + tabs(tab) + ']'

        def return_equation(eq:Equation, tab):
            string = ''
            for key in eq.data.keys():
                data = eq.data[key]
                if isinstance(data, list):
                    string += tabs(tab + 1) + f'{key}: {return_list(data, tab + 1)},\n'
                elif isinstance(data, Equation) and key == 'pow':
                    string += tabs(tab + 1) + f'{key}: {return_equation(data, tab + 1)[2*(tab+1):]},\n'
                elif isinstance(data, Equation):
                    string += return_equation(data, tab + 1) + '\n'
                else:
                    string += tabs(tab + 1) + f'{key}: {data},\n'
            return tabs(tab) + '{\n' + string + tabs(tab) + '}'

        
        string = return_equation(self, 0)
        print(string)


    def to_string(self):
        return self.__str__()[1:-1] if self.data['const'] == 1 and self.data['pow'] == 1 else self.__str__()


    def print_step(self, func, other):
        # if isinstance(other, Equation):
        #     print(f"{func}:\n   self: {self.to_string()}\n   other: {other.to_string()}\n")
        # if isinstance(other, int):
        #     print(f"{func}:\n   self: {self.to_string()}\n   other: {other}\n")
        ...


    def simplify(self:Equation):
        self._is_changed = False

        # if self.data['const'] == 0:
        #     self._is_changed = True
        #     return self := 0
        
        # if self.data['pow'] == 0:
        #     self._is_changed = True
        #     return self := 1

        # if isinstance(self.data['func'], list):
        #     if self.data['func'][0] == 'mul':
        #         for i in range(1, len(self.data['func'])):
        #             el:Equation = self.data['func'][i]

        #             if el == 0:
        #                 self._is_changed = True
        #                 self = 0
        #                 break

        #             if isinstance(el, Union[int, float]):
        #                 self._is_changed = True
        #                 self.data['const'] *= el

        #             elif isinstance(el, Equation):
        #                 el.simplify()
                    

        return self.simplify() if self._is_changed and isinstance(self, Equation) else self 


    def copy(eq:Equation):
        const:Union[int, float] = eq.data['const']
        func:Union[str, list[str, Equation]] = eq.data['func']
        power:Union[int, Equation] = eq.data['pow']

        def copy_power(eq:Union[int, float, Equation]):
            if isinstance(eq, Equation):
                return eq.copy()
            return eq
            
        if func == 'x':
            return Equation(const, 'x', copy_power(power))
        
        if isinstance(func, list):
            arr = []
            arr.append(func[0])

            for el in func[1:]:
                arr.append(el.copy() if isinstance(el, Equation) else el)
            
            return Equation(const, arr, copy_power(power))

        raise Exception(f"I can't copy this equation: {eq}")


