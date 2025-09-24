from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("calculate_years")

    assert in_code(ast.While)
    assert not_in_code(ast.For)
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)

@passed(has_functions)
@test(10)
def checks_calculate_years(test):
    """functie `calculate_years` werkt correct"""
    calculate_years = get_function("calculate_years")
    assert calculate_years(1200, 1300) ==   1
    assert calculate_years(20, 100) ==  20
    assert calculate_years(100, 1000000) == 115
    assert calculate_years(50, 600) ==  32
    assert calculate_years(9, 18) ==   8

@passed(has_functions)
@test(20)
def check_overall2(test):
    """kan overweg met foute invoer"""
    output = run(6, 9, 5, -6, 18)
    assert_output(output.number(), "8")
