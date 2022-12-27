from diffpy.diffmath.homogeneous import homogeneous
from diffpy.derivative import differentiate
from diffpy.integral import integrate
from diffpy.equation.Equation import Equation



def variation(a, b, c, eq:Equation):
    """
    A function created to solve 2nd order differential equations by using `variation of parameters`
    =============================================================================================
    
    Formulas:

    y_c = c1*y1 + c2*y2

    v1'*y1 + x2'*y2 = 0
    v1'*y1' + x2'*y2' = eq

    y1 = a, y2 = b, y1' = c, y2' = d

    det = (a * d) - (b * c)

    v1' = ( (0*y2') - (y2*eq) ) / det

    v1 = integral(v1')

    v2' = ( (y1*eq) - (0*y1') ) / det

    v2 = integral(v2')

    y_p = v1 * y1 + v2 * y2
    """
    
    try:
        return _variation(a, b, c, eq)
    except Exception as e:
        raise e


def _variation(a, b, c, eq:Equation):
    string, l = homogeneous(a, b, c)

    a = l[0]
    b = l[1]
    c = differentiate(a)
    d = differentiate(b)

    det = (d * a) - (b * c)

    v1_prime = ((-1 * (eq.copy() * b)) / det)
    v1 = integrate(v1_prime)
    
    v2_prime = (a * eq.copy()) / det 
    v2 = integrate(v2_prime)

    y_part:Equation = v1 * l[0] + v2 * l[1]
    
    return f'y = {string} + {y_part.to_string()}'
