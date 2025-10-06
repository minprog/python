from checkpy import *
from _pyprog_tools import *
from _list_tracking import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("merge_lists")

@passed(has_functions)
def test_merge_lists_result(test):
    """functie `merge_lists` geeft een gesorteerde lijst terug"""
    merge_lists = get_function("merge_lists")
    assert merge_lists([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_lists([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]
    assert merge_lists([1, 2, 5], [4, 5, 6]) == [1, 2, 4, 5, 5, 6]
    assert merge_lists([], []) == []
    assert merge_lists([1, 1, 1, 1], []) == [1, 1, 1, 1]
    assert merge_lists([], [1, 1, 1, 1]) == [1, 1, 1, 1]

@passed(has_functions)
def test_merge_lists1(test):
    """functie `merge_lists` gebruikt daadwerkelijk selection sort"""
    # lees file via checkpy API, voeg weer \n toe na splitten
    import re
    file_contents = [f"{x}\n" for x in static.getSource().split("\n")]
    srcCode = ("""
class HistoryList(list):
    def __init__(self, *args):
        super().__init__(*args)
        # Store a copy of the initial state
        self.history = [self.copy()]

    def __setitem__(self, index, value):
        super().__setitem__(index, value)
        # Save snapshot of the entire list
        self.history.append(self.copy())

    def append(self, value):
        super().append(value)
        # Save snapshot after append
        self.history.append(self.copy())

    def __delitem__(self, index):
        super().__delitem__(index)
        # Save snapshot of the entire list
        self.history.append(self.copy())

            """ + "\n\n")
    for line in file_contents:
        line = re.sub(r"=\s*\[\]", "= HistoryList()", line)
        line = re.sub(r"\blist\b", "HistoryList", line)
        srcCode += line

    test = [1, 2, 4], [3, 5, 6]
    expected_steps = [
        [1],
        [1, 2],
        [1, 2, 3],
        [1, 2, 3, 4],
        [1, 2, 3, 4, 5],
        [1, 2, 3, 4, 5, 6],
    ]
    result = getFunction("merge_lists", src=srcCode)(*test)
    if not is_subsequence(expected_steps, result.history):
        raise AssertionError(
            f"er gaat minstens één merge-stap niet zoals verwacht!\n"
            f"getest met merge_lists({test})\n"
            f"na de eerste stap zou de lijst dit moeten bevatten:\n"
            f"{expected_steps[0]}\n"
            f"de implementatie gaat mis bij deze en/of latere stappen")
