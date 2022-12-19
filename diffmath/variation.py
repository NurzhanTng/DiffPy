from diffpy.diffmath.homogeneous import homogeneous
from diffpy.derivative import differentiate
from diffpy.integral import integrate
from diffpy.equation.Equation import Equation



def variation(a, b, c, eq:Equation):
    try:
        return _variation(a, b, c, eq)
    except Exception as e:
        print(e)


def _variation(a, b, c, eq:Equation):
    string, l = homogeneous(a, b, c)

    a = l[0]
    b = l[1]
    c = differentiate(a)
    d = differentiate(b)

    det = (a * d) - (b * c)

    v1_prime = -(1 * (eq * b)) / det
    v1 = integrate(v1_prime)

    v2_prime = (a * eq) / det 
    v2 = integrate(v2_prime)

    y_part:Equation = v1 * l[0] + v2 * l[1]
    
    return f'y = {string} + {y_part.to_string()}'
