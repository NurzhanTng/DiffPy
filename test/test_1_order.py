from diffpy.equation.Variable import Variable
from diffpy.constants import e
from diffpy.diffmath.first_order import first_order



def test_1_order():
    x = Variable()
   
    eq1 = -2
    eq2 = -1 * e ** x
    assert first_order(eq1, eq2) == 'y = (e^(-1*x) + C) * e^(2*x)'

    eq1 = -3 / x
    eq2 = -1 * x
    assert first_order(eq1, eq2) == 'y = (x^-1 + C) * x^3.0'