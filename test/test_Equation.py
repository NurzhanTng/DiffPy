from diffpy.equation.Equation import Equation
from diffpy.equation.Variable import Variable


def test_Equation_add():
    x = Variable()

    assert (x + 5).to_dictionary() == {'const': 1, 'func': ['sum', {'const': 1, 'func': 'x', 'pow': 1}, 5], 'pow': 1}

    assert (5 + (x + 5) + x + (4 + x)).to_dictionary() == {'const': 1, 'func': ['sum', {'const': 3.0, 'func': 'x', 'pow': 1}, 9, 5.0], 'pow': 1}

    print('"test_Equation_add" is passed')


def test_Equation_mul():
    x = Variable()

    assert (x * 5).to_dictionary() == {'const': 5, 'func': 'x', 'pow': 1}

    assert ((5 + (x + 5)) * (x + (4 + x))).to_dictionary() == {'const': 1, 'func': ['mul', {'const': 1, 'func': ['sum', {'const': 1, 'func': 'x', 'pow': 1}, 5, 5.0], 'pow': 1}, {'const': 1, 'func': ['sum', {'const': 2.0, 'func': 'x', 'pow': 1}, 4], 'pow': 1}], 'pow': 1}

    print('"test_Equation_mul" is passed')

