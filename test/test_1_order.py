from diffpy.equation.Variable import Variable
from diffpy.constants import e
from diffpy.diffmath.first_order import first_order



def test_1_order():
    x = Variable()
   
    eq1 = -2
    eq2 = -1 * e ** x
    print(first_order(eq1, eq2))

    eq1 = -3 / x
    eq2 = -1 * x
    print(first_order(eq1, eq2)) 