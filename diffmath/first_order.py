from diffpy.integral.integrate import integrate
from diffpy.constants import e



def first_order(eq1, eq2):
    '''
    y = u*v
    y' = u'*v + u*v'
    u'*v + u*v' +/- p(x)*u*v = f(x)

    v' +/- p(x)*v = 0 - A part
    v' = +/- p(x)*v
    ln(v) = integral(+/- p(x))dx
    v = e^(integral(+/- p(x))dx)

    u'*v = f(x) - B part
    u' = f(x)/v
    u = integral(f(x)/v)dx
    '''

    # A part  
    P = integrate(eq1)

    if 'ln' in str(P):
        v = P[2:]
    else:
        v = e**(P)


    # B part
    u = integrate(eq2 / v) # + C [constanta]

    y = u*v
    string = f'y = ({u} + C) * {v}'

    return string, y