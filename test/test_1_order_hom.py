from diffpy.equation.Variable import Variable
from diffpy.diffmath.first_order_homogeneous import first_order_homogeneous

def test_1_order_hom():
    x = Variable()

    assert first_order_homogeneous(1, -1 / x) == "y = C * x"

    assert first_order_homogeneous(1, -1 * x ** 2) == "y = C * e^(0.3333333333333333*x^3)"
    
    print('"test_1_order_hom" is passed')