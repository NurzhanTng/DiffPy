"""
DiffPy is a Python library for discrete mathematics. It aims to become
a fully functional computer algebra system (CAS), while keeping
the code as simple as possible so that it is understandable and easily extensible.  
DiffPy is written entirely in Python. DiffPy is also able to solve problems 
related to finding derivatives and integrals of complex functions

Contact us for more information:

    Tangatarov Nurzhan: https://t.me/Tngtarov
    Syzdykova Meyirim: https://t.me/meyirimq
    Tuleugalieva Bibi: https://t.me/bbshkaaq

"""

from .equation import (Equation, Variable, Sin, Cos, Tan, Cot)

from .diffmath import (homogeneous, variation, undetermined_coefficient, first_order, first_order_homogeneous)

from .derivative import (differentiate)

from .integral import (integrate)

from .constants import (e, pi)



__all__ = [
    # diffpy.equation
    'Equation', 'Variable', 'Sin', 'Cos', 'Tan', 'Cot',

    # diffpy.diffmath
    'homogeneous', 'variation', 'undetermined_coefficient', 'first_order', 'first_order_homogeneous',
    
    # diffpy.integral.integrate
    'integrate',
    
    # diffpy.integral.integrate
    'differentiate',

    # diffpy.constants
    'e', 'pi'
]