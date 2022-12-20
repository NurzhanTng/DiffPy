from typing import Union

from diffpy.equation.Equation import Equation
from diffpy.equation.Variable import Variable
from diffpy.constants import (e, log)



def differentiate(eq:Union[int, float, Equation]):
    if isinstance(eq, Union[int, float]):
        return 0
    if not isinstance(eq, Equation):
        raise Exception(f'Equation is not class int, float or Equation types: Equation = {eq} ({type(eq)})')
    
    res = Exception(f"I can't solve this equation {eq}")
    if eq.data['func'] == 'x':
        res = _diff_x(eq)
    elif eq.data['func'] == '':
        res = _diff_exponent(eq)
    elif isinstance(eq.data['func'], list):
        if eq.data['func'][0] in ['sin', 'cos', 'tan', 'cot']:
            res = _diff_trigonometry(eq, eq[0])
        elif eq.data['func'][0] == 'sum':
            res = _diff_sum(eq)
        elif eq.data['func'][0] == 'mul':
            res = _diff_mul(eq)
    
    if isinstance(res, Exception):
        raise res
    if isinstance(res, Equation):
        res = res.simplify()
    return res



def _diff_x(eq:Equation):
    const:Union[int, float] = eq.data['const']
    power:Union[int, Equation] = eq.data['pow'] * 1

    if isinstance(power, Equation):
        return Exception(f"I can't solve this equation {eq}")
    
    res = Equation(const*power, 'x', power-1) if power != 1 else const

    eq.print_step('_diff_x', res)
    return res


def _diff_exponent(eq:Equation):
    const:Union[int, float] = eq.data['const']
    power:Equation = eq.data['pow']
    res = Exception(f"I can't solve this equation {eq}")

    if int(const / e) == const / e:
        res = differentiate(power) *  eq
    else:
        res = differentiate(power) * eq * log(const)

    eq.print_step('_diff_exponent', res)
    return res


def _diff_trigonometry(eq:Equation): NotImplemented


def _diff_sum(eq:Equation):
    const:Union[int, float] = eq.data['const']
    func:Union[str, list[str, Equation]] = eq.data['func']
    power:Union[int, Equation] = eq.data['pow']

    if power != 1:
        return Exception(f"I can't solve this equation {eq}")
    
    equations = func[2:]
    res = differentiate(func[1])
    for equation in equations:
        res += differentiate(equation)
    
    eq.print_step('_diff_sum', res * const)
    return res * const


def _diff_mul(eq:Equation):
    const:Union[int, float] = eq.data['const']
    func:Union[str, list[str, Equation]] = eq.data['func']
    power:Union[int, Equation] = eq.data['pow']

    if power != 1 or len(func[1:]) > 2:
        return Exception(f"I can't solve this equation {eq}")

    u = func[1]
    v = func[2]
    u1 = differentiate(u)
    v1 = differentiate(v)
    res = u1*v + u*v1
    
    eq.print_step('_diff_mul', res * const)
    return res * const
