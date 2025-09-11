from checkpy import *
from _static_analysis import *

# TODO modernize
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("check_coin")
    assert defines_function("determine_due")

    assert in_code(ast.While)
    assert not_in_code(ast.For)
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_in_code(ast.In)

@passed(has_functions)
@test(10)
def checks_coin(test):
    """functie `check_coin` werkt correct"""
    coin = getFunction("check_coin", test.fileName)
    assert_return(True, coin, 25)
    assert_return(True, coin, 10)
    assert_return(True, coin, 5)
    assert_return(False, coin, 1)
    assert_return(False, coin, 2)
    assert_return(False, coin, "10")

@passed(has_functions)
@test(20)
def checks_due(test):
    """functie `determine_due` werkt correct"""
    due = getFunction("determine_due", test.fileName)
    if due(50, 20) == 30:
        raise AssertionError("functie accepteert een munt van 20 cent, maar deze bestaat niet")
    assert_return(25, due, 50, 25)
    assert_return(50, due, 50, 20)
    assert_return(40, due, 50, 10)

@passed(has_functions)
@test(30)
def checks_main(test):
    """wisselgeld van 10 cent wordt verkregen na invoeren van 25, 10, en dan 25 cent"""
    output = run(25, 10, 25)
    assert output.strip()[-2:] == "10"
