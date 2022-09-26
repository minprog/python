import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *


@t.test(0)
def checks_compute_score(test):
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
    test.description = lambda: "De functie 'compute_score' werkt correct."


@t.test(1)
def check_S1(test):
    targets = ["Speler 1 wint!", "Player 1 wins!"]

    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=["Pizza", "Kaas"],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return any([asserts.exact(output.strip(), target) for target in targets])

    test.test = testMethod
    test.description = lambda: "Player 1 with 'Pizza' wins from Player 2 with 'Kaas'."


@t.test(2)
def check_S2(test):
    targets = ["Speler 2 wint!", "Player 2 wins!"]

    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=["Hotel", "Kamperen"],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return any([asserts.exact(output.strip(), target) for target in targets])

    test.test = testMethod
    test.description = (
        lambda: "Player 1 with 'Hotel' loses from Player 2 with 'Kamperen'."
    )


@t.test(3)
def check_gelijkspel(test):
    targets = ["Gelijkspel!", "It's a tie!"]

    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=["Vrijdag", "Zaterdag"],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return any([asserts.exact(output.strip(), target) for target in targets])

    test.test = testMethod
    test.description = (
        lambda: "Player 1 with 'Vrijdag' ties against Player 2 with 'Zaterdag'."
    )


@t.test(4)
def check_gelijkspel(test):
    targets = ["Gelijkspel!", "It's a tie!"]

    def testMethod():
        output = lib.outputOf(
            test.fileName,
            stdinArgs=["Hardly?", "Hardly!"],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return any([asserts.exact(output.strip(), target) for target in targets])

    test.test = testMethod
    test.description = (
        lambda: "Player 1 with 'Hardly?' ties against Player 2 with 'Hardly!'."
    )
