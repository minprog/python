import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics import *

"""
TODO:
- check of geod te groot en te klein wordt geprint
- check programma overall (als niet goed geraden opnieuw prompten)
"""

@t.test(0)
def checks_check_guess(test):
    def testMethod():
        check_guess = lib.getFunction("check_guess", test.fileName)
        if check_guess(10, 10) and not check_guess(5, 10):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'check_guess' werkt correct"

@t.test(1)
def checks_decide_number(test):
    def testMethod():
        decide_number = lib.getFunction("decide_number", test.fileName)
        if (decide_number(1000) != decide_number(1000) and decide_number(1) == 1
            and decide_number(3) <= 3):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'decide_number' werkt correct"

@t.test(2)
def check_level1(test):
    targets = ["gefeliciteerd", "congratulations"]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[1, 1],
            overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.contains(output, target) for target in targets])

    test.test = testMethod
    test.description = lambda : "bij level 1 wordt het getal 1 herkend als winnaar"

@t.test(2)
def check_overall(test):
    targets = ["gefeliciteerd", "congratulations"]
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
            overwriteAttributes = [("__name__", "__main__")])
        return any([asserts.contains(output, target) for target in targets])

    test.test = testMethod
    test.description = lambda : "bij level 10 wordt na maximaal 10 keer raden het getal goedgekeurd"
