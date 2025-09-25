# Track change history of a list object
#
# Example:
#
#     arg = HistoryList([1, 3])
#     result = getFunction("contig")(arg)
#     if len(arg.history) > 1:
#       raise AssertionError("originele lijst is toch aangepast")

class HistoryList(list):
    """
    A subclassed list object that keeps track of any changes made to it,
    or more precisely: the history of states of the list.

    Changes not tracked yet: extend, insert, pop, remove, clear
    """
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

def is_subsequence(pattern, target):
    """
    Check if `pattern` (list of lists) appears in `target` (list of lists),
    in the same order, but not necessarily consecutively.
    """
    it = iter(target)
    return all(any(p == t for t in it) for p in pattern)
