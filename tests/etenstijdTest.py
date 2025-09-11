from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functie `meal` is aanwezig"""
    assert defines_function("meal")
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    # assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@passed(has_functions)
@test(8)
def correct_meal_if_meal(test):
    """functie 'meal' geeft de juiste maaltijd voor elke tijd"""
    def testMethod():
        f = getFunction("meal", test.fileName)
        return (
            f('7:30') == 'ontbijt' and
            f('7:31') == 'ontbijt' and
            f('07:31') == 'ontbijt' and
            f('18:30') == 'avondeten' and
            f('13:00') == 'lunch' and
            f('12:00') == 'lunch'
        )
    test.test = testMethod

@passed(has_functions)
@test(9)
def correct_none_if_no_meal(test):
    """functie 'meal' geeft None als er geen maaltijd van toepassing is"""
    def testMethod():
        f = getFunction("meal", test.fileName)
        return (
            f('6:30') is None and
            f('8:01') is None and
            f('08:31') is None and
            f('14:01') is None and
            f('13:01') is None and
            f('17:59') is None
        )
    test.test = testMethod

@passed(has_functions)
@test(10)
def checks_breakfast(test):
    """bepaalt correct de tijd voor ontbijt"""
    correct_meal_descriptions = ["ontbijt", "breakfast"]

    output = run("7:25")
    assert any([meal in output for meal in correct_meal_descriptions])

    output = run("8:00")
    assert any([meal in output for meal in correct_meal_descriptions])

    output = run("8:01")
    assert not any([meal in output for meal in correct_meal_descriptions])

@passed(has_functions)
@test(20)
def checks_lunch(test):
    """bepaalt correct de tijd voor lunch"""
    correct_meal_descriptions = ["lunch"]

    output = run("13:00")
    assert any([meal in output for meal in correct_meal_descriptions])

    output = run("12:00")
    assert any([meal in output for meal in correct_meal_descriptions])

    output = run("13:40")
    assert not any([meal in output for meal in correct_meal_descriptions])

@passed(has_functions)
@test(30)
def checks_dinner(test):
    """bepaalt correct de tijd voor avondeten"""
    correct_meal_descriptions = ["avondeten", "dinner"]

    output = run("18:53")
    assert any([meal in output for meal in correct_meal_descriptions])

    output = run("18:00")
    assert any([meal in output for meal in correct_meal_descriptions])

    output = run("19:00")
    assert any([meal in output for meal in correct_meal_descriptions])

    output = run("19:59")
    assert not any([meal in output for meal in correct_meal_descriptions])
