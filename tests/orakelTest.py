from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `check_answer` is aanwezig"""
    assert function_defined_in_module("check_answer")

@passed(has_functions)
@test(10)
def checks_answer0(test):
    """het antwoord '42' geeft de uitvoer 'Ja'"""
    assert_output(run("42"), "Ja\n")

@passed(has_functions)
@test(20)
def checks_answer1(test):
    """het antwoord 'tweeenveertig' geeft de uitvoer 'Ja'"""
    assert_output(run("tweeenveertig"), "Ja\n")

@passed(has_functions)
@test(30)
def checks_answer2(test):
    """het antwoord 'tweeënveertig' geeft de uitvoer 'Ja'"""
    assert_output(run("tweeënveertig"), "Ja\n")

@passed(has_functions)
@test(40)
def checks_answer3(test):
    """het antwoord '53' geeft de uitvoer 'Nee'"""
    assert_output(run("53"), "Nee\n")
