from checkpy import *
from _pyprog_tools import *
from _list_tracking import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("special_sort")

@passed(has_functions)
def test_special_sort_result(test):
    """functie `special_sort` geeft een gesorteerde lijst terug"""
    special_sort = get_function("special_sort")
    assert special_sort([1,2,3]) == [1,2,3]
    assert special_sort([3,2,1]) == [1,2,3]
    assert special_sort([1,3,2,4]) == [1,2,3,4]
    assert special_sort([1]) == [1]
    assert special_sort([]) == []

@passed(has_functions)
def test_special_sort(test):
    """functie `special_sort` gebruikt echt "special" sort"""
    test = [4, 3, 2, 1]
    expected_steps = [
        [3, 4, 2, 1],
        [2, 4, 3, 1],
        [1, 4, 3, 2],
        [1, 3, 4, 2],
        [1, 2, 4, 3],
        [1, 2, 3, 4],
    ]
    to_sort = HistoryList(test.copy())
    result = getFunction("special_sort")(to_sort)
    if not is_subsequence(expected_steps, result.history):
        raise AssertionError(
            f"er gaat minstens één sorteer-stap niet zoals verwacht!\n"
            f"getest met special_sort({test})\n"
            f"na de eerste stap zou de lijst dit moeten bevatten:\n"
            f"{expected_steps[0]}\n"
            f"de implementatie gaat mis bij deze en/of latere stappen")
