import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts
from checkpy.entities import exception

from _basics import *
from _pyprog_tools import *

@t.passed(doctest_ok)
@t.test(9)
def checks_content(test):
    """datastructuur `list[list[int]]` is toegepast"""
    if not string_in_module("Board = list[list[int]]"):
        return False, "Board = list[list[int]] niet gevonden"
    if not string_in_module("def is_won(board: Board) -> bool:"):
        return False, "functie `is_won` moet een `board: Board`-parameter hebben"
    if not string_in_module("def print_board(board: Board) -> None:"):
        return False, "functie `print_board` moet een `board: Board`-parameter hebben"
    if not string_in_module("def create_board() -> Board:"):
        return False, "functie `create_board` moet een `Board` teruggeven"

@t.passed(checks_content)
@t.test(10)
def checks_set_board(test):
    """functie `create_board` werkt correct"""
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

@t.passed(checks_content)
@t.test(20)
def checks_is_won(test):
    """functie `is_won` werkt correct"""
    def testMethod():
        is_won = lib.getFunction("is_won", test.fileName)
        if (
            is_won([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]])
            and not is_won(
                [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 15]]
            )
        ):
            return True
        else:
            return False
    test.test = testMethod

@t.passed(checks_content)
@t.test(30)
def checks_move_tile(test):
    """functie `move_tile` werkt correct"""
    def testMethod():
        move_tile = lib.getFunction("move_tile", test.fileName)
        if not (
            move_tile([
                [15, 14, 13, 12],
                [11, 10, 9, 8],
                [7, 6, 5, 4],
                [3, 1, 2, 0],
            ], 2) == True
            and move_tile([
                [15, 14, 13, 12],
                [11, 10, 9, 8],
                [7, 6, 5, 4],
                [3, 1, 2, 0],
            ], 14) == False
        ):
            return False, "geeft de verkeerde return als een move wel/niet mogelijk is"

        board = [
            [15, 14, 13, 12],
            [11, 10, 9, 8],
            [7, 6, 5, 4],
            [3, 1, 2, 0],
        ]
        move_tile(board, 2)
        if not board == [
            [15, 14, 13, 12],
            [11, 10, 9, 8],
            [7, 6, 5, 4],
            [3, 1, 0, 2],
        ]:
            return False, "het bord wordt niet correct bijgewerkt na een move"

        return True
    test.test = testMethod

@t.passed(checks_content)
@t.test(40)
def check_win(test):
    """spel werkt en is uit te spelen"""
    def testMethod():
        steps = ["4","5","6","1","2","4","5","6",
                 "1","2","3","7","11","10","9","1",
                 "2","3","4","5","6","8","1","2",
                 "3","4","7","11","10","9","14",
                 "13","12","1","2","3","4","14",
                 "13","12","1","2","3","4","14",
                 "13","12","1","2","3","4","12",
                 "9","15","1","2","3","4","12","9",
                 "13","14","9","13","14","7","5",
                 "9","13","14","15","10","11","5",
                 "9","13","7","11","5","9","13",
                 "7","11","15","10","5","9","13",
                 "15","11","8","6","7","8","14",
                 "12","6","7","8","14","12","6",
                 "7","8","14","15","11","10","6",
                 "7","8","12","15","11","10","15",
                 "11","14","12","11","15","10",
                 "14","15","11","12"]

        try:
            output = lib.outputOf(test.fileName, stdinArgs=steps, overwriteAttributes=[("__name__", "__main__")]).splitlines()
        except exception.InputError:
            return False, "je programma lijkt niet te werken met de juiste oplossing voor het 4x4-board"

        return asserts.contains(output[-1], 'Gefeliciteerd') or asserts.contains(output[-1], 'Congratulations')
    test.test = testMethod
