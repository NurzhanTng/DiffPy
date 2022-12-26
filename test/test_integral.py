from diffpy.integral.integrate import integrate
from diffpy.equation.Variable import Variable
from diffpy.equation.trigonometric import (Sin, Cos)


def test_integral():
    x = Variable()

    assert integrate(3*x + 5).to_dictionary() == (1.5*x**2 + 5*x).to_dictionary()

    assert integrate(Sin(x)).to_dictionary() == (-1 * Cos(x)).to_dictionary()

    assert integrate(Cos(x)).to_dictionary() == Sin(x).to_dictionary()

    print('"test_integral" is passed')




