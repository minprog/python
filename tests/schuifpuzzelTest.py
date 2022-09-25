import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *


@t.test(0)
def checks_set_board(test):
    def testMethod():
        set_board = lib.getFunction("create_board", test.fileName)
        if set_board() == [
            [15, 14, 13, 12],
            [11, 10, 9, 8],
            [7, 6, 5, 4],
            [3, 1, 2, 0],
        ]:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda: "'create_board' works correctly."


@t.test(1)
def checks_is_won(test):
    def testMethod():
        is_won = lib.getFunction("is_won", test.fileName)
        if (
            is_won([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
            and not is_won([[1, 2, 3], [4, 5, 6], [8, 7, 0]])
            and not is_won(
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
            )
        ):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda: "'is_won' works correctly."


@t.test(2)
def checks_move_tile(test):
    def testMethod():
        move_tile = lib.getFunction("move_tile", test.fileName)
        if not (
            move_tile([[8, 7, 6], [5, 4, 3], [2, 1, 0]], 3) == True
            and move_tile([[8, 7, 6], [5, 4, 3], [2, 1, 0]], 7) == False
        ):
            return False, "Returning the wrong boolean for correct/incorrect moves."

        board = [[8, 7, 6], [5, 4, 3], [2, 1, 0]]
        move_tile(board, 1)
        if not board == [[8, 7, 6], [5, 4, 3], [2, 0, 1]]:
            return False, "Board does not correctly update after valid move."

        return True

    test.test = testMethod
    test.description = lambda: "'move_tile' works correctly."
