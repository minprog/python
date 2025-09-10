from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """functie `is_schrikkel` is aanwezig"""
    assert defines_function("is_schrikkel")

@passed(has_functions)
def test_weeks_elapsed(test):
    """functie `is_schrikkel` werkt correct"""
    assert getFunction("is_schrikkel")(2001) == False
    assert getFunction("is_schrikkel")(2000) == True
    assert getFunction("is_schrikkel")(1463) == False
    assert getFunction("is_schrikkel")(2020) == True
    assert getFunction("is_schrikkel")(2100) == False
    assert getFunction("is_schrikkel")(1900) == False

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert outputOf(stdinArgs=[2001],
        overwriteAttributes=[("__name__", "__main__")]
    ) == "2001 is geen schrikkeljaar\n"
    assert outputOf(stdinArgs=[2000],
        overwriteAttributes=[("__name__", "__main__")]
    ) == "2000 is een schrikkeljaar\n"
