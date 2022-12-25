from __future__ import annotations
from typing import Union

from diffpy.equation.Variable import Variable
from diffpy.equation.trigonometric import Sin, Cos
from diffpy.constants import e


def homogeneous(a:Union[int, float], b:Union[int, float], c:Union[int, float]):
    """

    """
    
    x = Variable()
    D = b**2 - 4*a*c

    if D == 0:
        root = -b / (2*a)

        y1 = e**(root * x)
        y2 = e**(root * x) * x

        string = f'C₁e^({root}x) + C₂e^({root}x) * x'
        l = [y1, y2]

    if D > 0:
        D = D ** 0.5
        root1 = (-b - D)/(2*a)
        root2 = (-b + D)/(2*a)

        y1 = e**(root1 * x)
        y2 = e**(root2 * x)

        string = f'C₁e^({root1}x) + C₂e^({root2}x)'
        l = [y1, y2]

    if D < 0:
        real_part = (-1 * b) / (2*a)
        im_part = (-1*D) ** 0.5 / (2*a)

        y1= e**(real_part * x) * (Cos(im_part * x))
        y2= e**(real_part * x) * (Sin(im_part * x))

        string = f'e^({real_part}x) * (C₁cos({im_part}x) + C₂sin({im_part}x))'
        l = [y1, y2]
 
    return string, l
