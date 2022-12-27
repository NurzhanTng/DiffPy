from diffpy import (e, Variable, variation)


def test_variation():
    x = Variable()

    print(variation(1, 1, -2, x * e**x),'\n\n')

    print(variation(1, 2, 1, e**x),'\n\n')

    print(variation(1, 0, -1, 2*x**2 - x - 3))