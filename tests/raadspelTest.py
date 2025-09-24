from checkpy import *
from _static_analysis import *

# TODO modernize
import checkpy.assertlib as asserts

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

"""
TODO:
- check of goed te groot en te klein wordt geprint
- check programma overall (als niet goed geraden opnieuw prompten)
"""

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("check_guess")
    assert function_defined_in_module("decide_number")

    assert construct_in_ast(ast.While)
    assert construct_not_in_ast(ast.For)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)

@passed(has_functions)
@test(10)
def checks_check_guess(test):
    """functie `check_guess` werkt correct"""
    check_guess = get_function("check_guess")
    assert check_guess(10, 10) == True
    assert check_guess(5, 10) == False

@passed(has_functions)
@test(20)
def checks_decide_number(test):
    """functie `decide_number` werkt correct"""
    decide_number = getFunction("decide_number", test.fileName)
    if (decide_number(1000) != decide_number(1000) and decide_number(1) == 1
        and decide_number(3) <= 3):
        return True
    else:
        raise AssertionError("de functie lijkt verkeerde of onlogische waarden op te leveren")

@passed(has_functions)
@test(30)
def check_level1(test):
    """bij level 1 wordt het getal 1 herkend als winnaar"""
    targets = ["gefeliciteerd", "congratulations"]
    output = run(1, 1)
    if any([asserts.contains(output, target) for target in targets]):
        return True
    else:
        raise AssertionError("level 1 en gok 1 zou een felicitatie moeten opleveren")

@passed(has_functions)
@test(40)
def check_overall(test):
    """bij level 10 wordt na maximaal 10 keer verschillend raden het getal goedgekeurd"""
    targets = ["gefeliciteerd", "congratulations"]
    output = run(10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
    if any([asserts.contains(output, target) for target in targets]):
        return True
    else:
        raise AssertionError
