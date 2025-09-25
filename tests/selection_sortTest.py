from checkpy import *
from _static_analysis import *
from _list_tracking import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("selection_sort")

@passed(has_functions)
def test_selection_sort_result(test):
    """functie `selection_sort` geeft een gesorteerde lijst terug"""
    selection_sort = get_function("selection_sort")
    assert selection_sort([1,2,3]) == [1,2,3]
    assert selection_sort([3,2,1]) == [1,2,3]
    assert selection_sort([1,3,2,4]) == [1,2,3,4]
    assert selection_sort([1]) == [1]
    assert selection_sort([]) == []

@passed(has_functions)
def test_selection_sort(test):
    """functie `selection_sort` gebruikt daadwerkelijk selection sort"""
    test = [5, 2, 1, 3, 6, 4]
    expected_steps = [
        [1, 2, 5, 3, 6, 4],
        [1, 2, 3, 5, 6, 4],
        [1, 2, 3, 4, 6, 5],
        [1, 2, 3, 4, 5, 6],
    ]
    to_sort = HistoryList(test.copy())
    result = getFunction("selection_sort")(to_sort)
    if not is_subsequence(expected_steps, result.history):
        raise AssertionError(
            f"er gaat minstens één sorteer-stap niet zoals verwacht!\n"
            f"getest met selection_sort({test})\n"
            f"na de eerste stap zou de lijst dit moeten bevatten:\n"
            f"{expected_steps[0]}\n"
            f"de implementatie gaat mis bij deze en/of latere stappen")
