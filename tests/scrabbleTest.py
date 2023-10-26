import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics_no_listcomp import *

@t.passed(doctest_ok)
@t.test(10)
def checks_compute_score(test):
    """functie 'compute_score' werkt correct"""
    def testMethod():
        compute_score = lib.getFunction("compute_score", test.fileName)
        if (
            compute_score("WORD") == compute_score("word")
            and compute_score("Test") == 4
            and compute_score("abcdefghijklmnopqrstuvwxyz") == 87
        ):
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def check_S1(test):
    """speler 1 met 'Pizza' wint van speler 2 met 'Kaas'"""
    targets = ["Speler 1 wint!", "Player 1 wins!"]

    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=["Pizza", "Kaas"],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return any([asserts.exact(output.strip(), target) for target in targets])
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def check_S2(test):
    """speler 1 met 'Hotel' verliest van speler 2 met 'Kamperen'"""
    targets = ["Speler 2 wint!", "Player 2 wins!"]

    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=["Hotel", "Kamperen"],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return any([asserts.exact(output.strip(), target) for target in targets])
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(40)
def check_gelijkspel(test):
    """speler 1 met 'Vrijdag' speelt gelijk met speler 2 met 'Zaterdag'"""
    targets = ["Gelijkspel!", "It's a tie!"]

    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=["Vrijdag", "Zaterdag"],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return any([asserts.exact(output.strip(), target) for target in targets])

    test.test = testMethod

@t.passed(doctest_ok)
@t.test(50)
def check_gelijkspel(test):
    """speler 1 met 'Hardly?' speelt gelijk met speler 2 met 'Hardly!'"""
    targets = ["Gelijkspel!", "It's a tie!"]

    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=["Hardly?", "Hardly!"],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return any([asserts.exact(output.strip(), target) for target in targets])

    test.test = testMethod
