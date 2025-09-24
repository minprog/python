from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("get_positive_int")
    assert function_defined_in_module("get_any_int_but_0")
    assert function_defined_in_module("get_min_int")
    assert function_defined_in_module("get_two_different_ints")

    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    # assert construct_not_in_ast(ast.Tuple) # return for get_two_different_ints is tuple
    assert construct_not_in_ast(ast.Dict)
    assert construct_not_in_ast(ast.In)
