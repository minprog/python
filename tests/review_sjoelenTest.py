import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.test(0)
def checks_calculate_points(test):
    def testMethod():
        calculate_points = lib.getFunction("calculate_points", test.fileName)
        if (calculate_points([7,2,3,4]) == 56 and calculate_points([4, 4, 4, 4]) == 80):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'calculate_points' works correctly."


@t.test(1)
def checks_calculate_points_board(test):
    def testMethod():
        calculate_points = lib.getFunction("calculate_points", test.fileName)
        board = [1,2,3,4]
        calculate_points(board)
        if board == [1, 2, 3, 4]:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "The board remains unchanged in 'calculate_points'."

@t.test(2)
def checks_shuffle_round(test):
    def testMethod():
        shuffle_round = lib.getFunction("shuffle_round", test.fileName)
        board = [0, 0, 0, 0]
        for i in range(10000):
            stones = shuffle_round(board, 100)
        board = [b / 10000 for b in board]
        if (6.5 < board[0] < 8.5 and 4 < board[1] < 6 and 4 < board[2] < 6 and
            6.5 < board[3] < 8.5):
            return True
        else:
            return False, board

    test.test = testMethod
    test.description = lambda : "'shuffle_round' simulates games with chances within the required ranges."
