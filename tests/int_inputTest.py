from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("get_positive_int")
    assert defines_function("get_any_int_but_0")
    assert defines_function("get_min_int")
    assert defines_function("get_two_different_ints")

    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    # assert not_in_code(ast.Tuple) # return for get_two_different_ints is tuple
    assert not_in_code(ast.Dict)
    assert not_in_code(ast.In)
