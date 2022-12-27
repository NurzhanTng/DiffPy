from diffpy import (undetermined_coefficient, Variable, Sin, Cos)


def test_undetermined_coefficient():
    x = Variable()

    eq1 = 5*Cos(2*x) + 10*Sin(2*x)
    assert undetermined_coefficient(1, -2, 1, eq1) == "y = C₁e^(1.0x) + C₂e^(1.0x) * x - 2.0sin(2x) + 1.0cos(2x)"

    eq2 = 1 - 3*x + 6*x**2
    assert undetermined_coefficient(1, -4, 4, eq2) == "y = C₁e^(2.0x) + C₂e^(2.0x) * x + (1.5*x^2 + 2.25*x + 2.75)"

    print('"test_undetermined_coefficient" is passed')