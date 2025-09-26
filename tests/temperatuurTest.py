from checkpy import *
from _pyprog_tools import *

from _python_checks import forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()

@passed(has_functions)
@test(10)
def checks_convert_temperature(test):
    """functie 'convert_temperature' werkt correct"""
    convert_temperature = get_function("convert_temperature")
    assert convert_temperature("C", 10) == 50
    assert convert_temperature("F", 9) == -12

@passed(has_functions)
@test(20)
def check_overall1(test):
    """print juiste tabel voor F naar C met start 0, eind 9 en stapgrootte 3"""
    assert run("F", 0, 9, 3).strip() ==        "F |   C\n  0 | -17\n  3 | -16\n  6 | -14\n  9 | -12"

@passed(has_functions)
@test(30)
def check_overall2(test):
    """print juiste tabel voor C naar F met start 0, eind 20 en stapgrootte 5"""
    assert run("C", 0, 20, 5).strip() ==        "C |   F\n  0 |  32\n  5 |  41\n 10 |  50\n 15 |  59\n 20 |  68"

@passed(has_functions)
@test(40)
def check_overall3(test):
    """print juiste tabel voor f (lowercase) naar C met start 0, eind 9 en stapgrootte 3"""
    assert run("f", 0, 9, 3).strip() ==        "F |   C\n  0 | -17\n  3 | -16\n  6 | -14\n  9 | -12"
