from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("selection_sort")

@passed(has_functions)
def test_selection_sort_result(test):
    """functie `selection_sort` geeft een gesorteerde lijst terug"""
    assert getFunction("selection_sort")([1,2,3]) == [1,2,3]
    assert getFunction("selection_sort")([3,2,1]) == [1,2,3]
    assert getFunction("selection_sort")([1,3,2,4]) == [1,2,3,4]
    assert getFunction("selection_sort")([]) == []

class HistoryList(list):
    def __init__(self, *args):
        super().__init__(*args)
        # Store a copy of the initial state
        self.history = [self.copy()]

    def __setitem__(self, index, value):
        super().__setitem__(index, value)
        # Save snapshot of the entire list
        self.history.append(self.copy())

def is_subsequence(pattern, target):
    """
    Check if `pattern` (list of lists) appears in `target` (list of lists),
    in the same order, but not necessarily consecutively.
    """
    it = iter(target)
    return all(any(p == t for t in it) for p in pattern)

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
            f"getest met selection_sort({test})\n"
            f"na de eerste sorteer-stap zou het {expected_steps[0]} moeten zijn")
