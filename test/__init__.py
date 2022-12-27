"""
# A module for checking all methods implemented in the library

To test some method you should just call the corresponding function from this module 

If you see in the console `"test_name_of_method" is passed`, it means that the code is working `correctly`
If you see an `error`, it means that the method is `not completed`
"""


from diffpy.test.test_1_order import test_1_order
from diffpy.test.test_1_order_hom import test_1_order_hom
from diffpy.test.test_Equation import (test_Equation_add, test_Equation_mul)
from diffpy.test.test_homogeneous import test_homogeneous
from diffpy.test.test_integral import test_integral
from diffpy.test.test_undetermined_coefficient import test_undetermined_coefficient
from diffpy.test.test_variation import test_variation

__all__ = [
    "test_1_order", 
    "test_1_order_hom", 
    "test_Equation_add", 
    "test_Equation_mul", 
    "test_homogeneous", 
    "test_integral", 
    "test_undetermined_coefficient", 
    "test_variation",
]