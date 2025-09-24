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
    # assert not_in_code(ast.Tuple) # wordt aangeraden in de opdracht ivm split
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@passed(has_functions)
@test(8)
def correct_meal_if_meal(test):
    """functie `meal` geeft de juiste maaltijd voor elke tijd"""
    f = get_function("meal")
    assert f('7:30') == 'ontbijt'
    assert f('7:31') == 'ontbijt'
    assert f('07:31') == 'ontbijt'
    assert f('18:30') == 'avondeten'
    assert f('13:00') == 'lunch'
    assert f('12:00') == 'lunch'

@passed(has_functions)
@test(9)
def correct_none_if_no_meal(test):
    """functie `meal` geeft None als er geen maaltijd van toepassing is"""
    f = get_function("meal")
    assert f('6:30') == None
    assert f('8:01') == None
    assert f('08:31') == None
    assert f('14:01') == None
    assert f('13:01') == None
    assert f('17:59') == None

@passed(has_functions)
def checks_breakfast(test):
    """programma bepaalt correct de tijd voor ontbijt"""
    correct_meal_descriptions = ["ontbijt", "breakfast"]
    output = run("7:25"); assert_any(output, correct_meal_descriptions)
    output = run("8:00"); assert_any(output, correct_meal_descriptions)
    output = run("8:01"); assert_none(output, correct_meal_descriptions)

@passed(has_functions)
def checks_lunch(test):
    """programma bepaalt correct de tijd voor lunch"""
    correct_meal_descriptions = ["lunch"]
    output = run("13:00"); assert_any(output, correct_meal_descriptions)
    output = run("12:00"); assert_any(output, correct_meal_descriptions)
    output = run("13:40"); assert_none(output, correct_meal_descriptions)

@passed(has_functions)
def checks_dinner(test):
    """programma bepaalt correct de tijd voor avondeten"""
    correct_meal_descriptions = ["avondeten", "dinner"]
    output = run("18:53"); assert_any(output, correct_meal_descriptions)
    output = run("18:00"); assert_any(output, correct_meal_descriptions)
    output = run("19:00"); assert_any(output, correct_meal_descriptions)
    output = run("19:59"); assert_none(output, correct_meal_descriptions)
