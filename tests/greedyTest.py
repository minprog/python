from checkpy import *
from _static_analysis import *

# TODO modernize
import checkpy.lib as lib
import checkpy.assertlib as assertlib

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert not_in_code(ast.List)
    assert not_in_code(ast.For) # for-loop makes no sense here
    assert not_in_code(ast.Set)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_in_code(ast.In)

@passed(has_functions)
@test(10)
def exactChange0(test):
    """0$ aan wisselgeld staat gelijk aan 0 munten"""
    assert_output(run(0).number(), "0")

@passed(has_functions)
@test(20)
def exactChange41(test):
    """0.41$ aan wisselgeld staat gelijk aan 4 munten"""
    assert_output(run(0.41).number(), "4")

@passed(has_functions)
@test(30)
def exactChange9999(test):
    """9999$ aan wisselgeld staat gelijk aan 39996 munten"""
    assert_output(run(9999).number(), "39996")
    if has_string("39996"):
        raise AssertionError("de uitkomst 39996 moet berekend worden maar staat in de code\n"
            "mocht je deze in de doctests hebben staan, kies dan een ander voorbeeld")

@passed(has_functions)
@test(40)
def exactChange402(test):
    """4.02$ aan wisselgeld staat gelijk aan 18 munten"""
    assert_output(run(4.02).number(), "18")
    if has_string("18"):
        raise AssertionError("de uitkomst 18 moet berekend worden maar staat in de code\n"
            "mocht je deze in de doctests hebben staan, kies dan een ander voorbeeld")

@passed(has_functions)
@test(50)
def exactChange35(test):
    """0.35$ aan wisselgeld staat gelijk aan 2 munten"""
    assert_output(run(0.35).number(), "2")

@passed(has_functions)
@test(60)
def handlesWrongInput(test):
    """accepteert geen negatieve invoer"""
    assert_output(run(-1, -1, 0.41).number(), "4")
