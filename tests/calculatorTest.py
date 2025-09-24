from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `evaluate` is aanwezig"""
    assert defines_function("evaluate")
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    # assert not_in_code(ast.Tuple) # wordt aangeraden in de opdracht ivm split
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@passed(has_functions)
@test(10)
def checks_answer0(test):
    """3 + 5 = 8.0"""
    assert_output(run("3 + 5").strip(), "8.0")

@passed(has_functions)
@test(20)
def checks_answer1(test):
    """19 - 6 = 13.0"""
    assert_output(run("19 - 6").strip(), "13.0")

@passed(has_functions)
@test(30)
def checks_answer2(test):
    """6 - 19 = -13.0"""
    assert_output(run("6 - 19").strip(), "-13.0")

@passed(has_functions)
@test(40)
def checks_answer3(test):
    """12 * 23 = 276.0"""
    assert_output(run("12 * 23").strip(), "276.0")

@passed(has_functions)
@test(50)
def checks_answer4(test):
    """6 / 4 = 1.5"""
    assert_output(run("6 / 4").strip(), "1.5")

@passed(has_functions)
@test(60)
def checks_answer5(test):
    """-8 * 12 = -96.0"""
    assert_output(run("-8 * 12").strip(), "-96.0")
