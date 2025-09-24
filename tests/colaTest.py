from checkpy import *
from _static_analysis import *

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
    coin = get_function("check_coin")
    assert_no_input_output(coin)
    assert coin(25) == True
    assert coin(10) == True
    assert coin(5) == True
    assert coin(1) == False
    assert coin(2) == False
    assert coin("10") == False

@passed(has_functions)
@test(20)
def checks_due(test):
    """functie `determine_due` werkt correct"""
    due = get_function("determine_due")
    assert_no_input_output(due)
    if due(50, 20) == 30:
        raise AssertionError("functie accepteert een munt van 20 cent, maar deze bestaat niet")
    assert due(50, 25) == 25
    assert due(50, 20) == 50
    assert due(50, 10) == 40

@passed(has_functions)
@test(30)
def checks_main(test):
    """run: invoeren van 25, 10, en dan 25 cent geeft wisselgeld van 10 cent"""
    output = run(25, 10, 25)
    assert_output(output.strip()[-2:].number(), "10")
