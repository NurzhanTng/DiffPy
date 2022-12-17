from diffpy.equation import Equation, x


def Sin(eq):
    if isinstance(eq, x):
        eq = eq * 1
    return Equation(1, ['sin', eq], 1)

def Cos(eq):
    if isinstance(eq, x):
        eq = eq * 1
    return Equation(1, ['cos', eq], 1)

def Tg(eq):
    if isinstance(eq, x):
        eq = eq * 1
    return Equation(1, ['tg', eq], 1)

def Ctg(eq):
    if isinstance(eq, x):
        eq = eq * 1
    return Equation(1, ['ctg', eq], 1)