from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("spongebob1")
    assert function_defined_in_module("spongebob2")
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)

@passed(has_functions)
def test_function_spongebob1(test):
    """functie `spongebob1` werkt correct"""
    spongebob1 = get_function("spongebob1")
    assert spongebob1('hello world!') == 'hElLo wOrLd!'
    assert spongebob1('orwellian') == 'oRwElLiAn'
    assert spongebob1("") == ""

@passed(has_functions)
def test_function_spongebob2(test):
    """functie `spongebob2` werkt correct"""
    spongebob2 = get_function("spongebob2")
    assert spongebob2('hello world!') == 'hElLo WoRlD!'
    assert spongebob2('orwellian') == 'oRwElLiAn'
    assert spongebob2("") == ""
