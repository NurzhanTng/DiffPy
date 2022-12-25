from typing import Union

from diffpy.equation.Equation import Equation
from diffpy.constants import (e, log)
from diffpy.equation.trigonometric import (Sin, Cos, Tan, Cot)



def integrate(eq:Union[int, float, Equation]):
    """

    """

    if isinstance(eq, Equation):
        eq = eq.copy()

    if isinstance(eq, Union[int, float]):
        return Equation(eq, 'x', 1)
    if not isinstance(eq, Equation):
        raise Exception(f'Equation is not class int, float or Equation types: Equation = {eq} ({type(eq)})')
    
    res = Exception(f"I can't solve this equation {eq}")

    if eq.data['func'] == 'x':
        res = _integ_x(eq)
    
    elif eq.data['func'] == '':
        res = _integ_exponent(eq)
    
    elif isinstance(eq.data['func'], list):
        if eq.data['func'][0] in ['sin', 'cos', 'tan', 'cot']:
            res = _integ_trigonometry(eq)
    
        elif eq.data['func'][0] == 'sum':
            res = _integ_sum(eq)
    
        elif eq.data['func'][0] == 'mul':
            res = _integ_mul(eq)
    
    if isinstance(res, Exception):
        raise res
    if isinstance(res, Equation):
        res = res.simplify()
        
    return res




def _integ_x(eq:Equation):
    const:Union[int, float] = eq.data['const']
    power:Union[int, Equation] = eq.data['pow'] * 1

    if isinstance(power, Equation):
        return Exception(f"I can't solve this equation {eq}")

    if power != -1:
        res = Equation(const/(power+1), 'x', power+1)
    else:
        return Exception(f"I doesn't created ln yet, so I can't integrate this eq: {eq}")

    eq.print_step('_integ_x', res)
    return res



def _integ_exponent(eq:Equation):
    const:Union[int, float] = eq.data['const']
    power:Equation = eq.data['pow']
    res = Exception(f"I can't solve this equation {eq}")

    if int(const / e) == const / e:
        res = integrate(power) / eq
    else:
        res = integrate(power) / (eq * log(const))

    eq.print_step('_integ_exponent', res)
    return res



def _integ_trigonometry(eq:Equation):
    const:Union[int, float] = eq.data['const']
    func_name:str = eq.data['func'][0]
    func_arg:Equation = eq.data['func'][1]
    power:Union[int, Equation] = eq.data['pow']

    if len(eq.data['func']) > 2:
        return Exception(f"Wrong format of equation: {eq.show_data()}")

    if func_name == 'sin':
        return _integ_sin(const, power, func_arg)
    if func_name == 'cos':
        return _integ_cos(const, power, func_arg)
    if func_name == 'tan':
        return _integ_tan(const, power, func_arg)
    if func_name == 'cot':
        return _integ_cot(const, power, func_arg)


def _integ_sin(const, power, arg):
    if power == 1:
        if arg.data['func'] == 'x' and  arg.data['pow'] == 1:
            return Cos(arg) * const
    else:
        return Exception(f"I can't solve this equation: {Equation(const, ['sin', arg], power)}")

def _integ_cos(const, power, arg:Equation):
    if power == 1:
        if arg.data['func'] == 'x' and  arg.data['pow'] == 1:
            return Sin(arg) * const
    else:
        return Exception(f"I can't solve this equation: {Equation(const, ['sin', arg], power)}")

def _integ_tan(const, power, arg):
    return Exception(f"I can't solve this equation: {Equation(const, ['sin', arg], power)}")

def _integ_cot(const, power, arg):
    return Exception(f"I can't solve this equation: {Equation(const, ['sin', arg], power)}")



def _integ_sum(eq:Equation):
    eq = eq.copy()

    const:Union[int, float] = eq.data['const']
    func:Union[str, list[str, Equation]] = eq.data['func']
    power:Union[int, Equation] = eq.data['pow']

    if power != 1:
        return Exception(f"I can't solve this eq {eq}")
    
    equations = func[2:]
    res = integrate(func[1])
    for equation in equations:
        res += integrate(equation)
    
    eq.print_step('_integ_sum', res * const)
    return res * const



def _integ_mul(eq:Equation): return Exception(f"I can't integrate complex equation {eq}")
