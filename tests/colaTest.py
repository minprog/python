from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("check_coin")
    assert function_defined_in_module("determine_due")

    assert construct_in_ast(ast.While)
    assert construct_not_in_ast(ast.For)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert construct_not_in_ast(ast.In)

@passed(has_functions)
@test(10)
def checks_coin(test):
    """functie `check_coin` werkt correct"""
    coin = get_function("check_coin")
    assert no_input_output_in_function(coin)
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
    due = getFunction("determine_due")
    assert no_input_output_in_function(due)
    if due(50, 20) == 30:
        raise AssertionError("functie accepteert een munt van 20 cent, maar deze bestaat niet")
    due = get_function("determine_due")
    assert due(50, 25) == 25
    assert due(50, 20) == 50
    assert due(50, 10) == 40

@passed(has_functions)
@test(30)
def checks_main(test):
    """run: invoeren van 25, 10, en dan 25 cent geeft wisselgeld van 10 cent"""
    assert run(25, 10, 25).strip()[-2:].number() == "10"
