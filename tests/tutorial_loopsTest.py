from checkpy import *
from _pyprog_tools import *

from _check_doctests import check_doctests

import _catch_syntax_error
from _catch_syntax_error import no_syntax_error
_catch_syntax_error.MAX_SYNTAX_ERRORS = 2

def prints(name, expected):
    """Checks that calling `name` prints the expected lines and returns None."""
    assert function_defined_in_module(name)
    f = getFunction(fname(name))
    result = f()
    got = f.printOutput.split()
    want = [str(x) for x in expected]
    if got != want:
        raise AssertionError(
            f"bij een aanroep van {name}(): verwachtte de regels {want!r} maar kreeg {got!r}")
    if result is not None:
        raise AssertionError(f"{name} moet niets returnen, maar gaf {result!r}")
    return True

@test()
def test_print_one_to_five():
    """functie `print_one_to_five` werkt correct"""
    assert prints("print_one_to_five", [1, 2, 3, 4, 5])

@test()
def test_print_squares():
    """functie `print_squares` werkt correct"""
    assert prints("print_squares", [1, 4, 9, 16, 25, 36])

@test()
def test_print_fives():
    """functie `print_fives` werkt correct"""
    assert prints("print_fives", [5, 10, 15, 20, 25, 30])

@test()
def test_print_sevens():
    """functie `print_sevens` werkt correct"""
    assert prints("print_sevens", [7, 14, 21, 28, 35, 42, 49])

@test()
def test_print_countdown():
    """functie `print_countdown` werkt correct"""
    assert prints("print_countdown", [5, 4, 3, 2, 1])

@test()
def test_print_down_by_three():
    """functie `print_down_by_three` werkt correct"""
    assert prints("print_down_by_three", [20, 17, 14, 11, 8, 5, 2, -1])

@test()
def test_print_with_exclamations():
    """functie `print_with_exclamations` werkt correct"""
    assert prints("print_with_exclamations", [1, 2, 3, 4, "!", 6, 7, 8, 9, "!", 11, 12])

@test()
def test_print_odds_only():
    """functie `print_odds_only` werkt correct"""
    assert prints("print_odds_only", [1, "x", 3, "x", 5, "x", 7, "x", 9, "x"])

@test()
def test_print_doublings():
    """functie `print_doublings` werkt correct"""
    assert prints("print_doublings", [1, 2, 4, 8, 16, 32])

@test()
def test_print_fives_powers():
    """functie `print_fives_powers` werkt correct"""
    assert prints("print_fives_powers", [1, 5, 25, 125, 625])

@test()
def test_print_halvings():
    """functie `print_halvings` werkt correct"""
    assert prints("print_halvings", [100, 50, 25, 12, 6, 3, 1, 0, 0])

@test()
def test_print_thirds():
    """functie `print_thirds` werkt correct"""
    assert prints("print_thirds", [729, 243, 81, 27, 9, 3, 1, 0, 0])

@test()
def test_is_leap_year():
    """functie `is_leap_year` werkt correct"""
    assert function_defined_in_module("is_leap_year")
    f = get_function("is_leap_year")
    assert f(2024).is_(True)
    assert f(2023).is_(False)
    assert f(1900).is_(False)
    assert f(2000).is_(True)

@test()
def test_count_leap_years():
    """functie `count_leap_years` werkt correct"""
    assert function_defined_in_module("count_leap_years")
    f = get_function("count_leap_years")
    assert f(2000, 2001) == 1
    assert f(2020, 2024) == 2
    assert f(1800, 1900) == 24
    assert f(2001, 2003) == 0
    assert f(2024, 2024) == 1

@test()
def test_nth_leap_year():
    """functie `nth_leap_year` werkt correct"""
    assert function_defined_in_module("nth_leap_year")
    f = get_function("nth_leap_year")
    assert f(2000, 1) == 2000
    assert f(1800, 1) == 1804
    assert f(2000, 3) == 2008
    assert f(1896, 3) == 1908
    assert f(2001, 10) == 2040

@test()
def test_is_prime():
    """functie `is_prime` werkt correct"""
    assert function_defined_in_module("is_prime")
    f = get_function("is_prime")
    assert f(2).is_(True)
    assert f(3).is_(True)
    assert f(7919).is_(True)
    assert f(1).is_(False)
    assert f(4).is_(False)
    assert f(7920).is_(False)

@test()
def test_print_prime_list():
    """functie `print_prime_list` werkt correct"""
    assert function_defined_in_module("print_prime_list")
    f = getFunction(fname("print_prime_list"))
    result = f(30)
    want = ["2", "3", "5", "7", "11", "13", "17", "19", "23", "29"]
    got = f.printOutput.split()
    if got != want:
        raise AssertionError(
            f"bij een aanroep van print_prime_list(30): verwachtte de regels {want!r} maar kreeg {got!r}")
    if result is not None:
        raise AssertionError(f"print_prime_list moet niets returnen, maar gaf {result!r}")
    f(2)
    got = f.printOutput.split()
    if got != []:
        raise AssertionError(
            f"bij een aanroep van print_prime_list(2): verwachtte geen regels maar kreeg {got!r}")

@test(100)
def doctests(test):
    """elke functie heeft voldoende doctests en ze geven allemaal akkoord"""
    def testMethod():
        return check_doctests(test, True)
    test.test = testMethod
    test.fail = lambda info: info
    test.timeout = lambda: 120
