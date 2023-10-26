import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics_no_listcomp import *

@t.passed(doctest_ok)
@t.test(10)
def checks_answer0(test):
    """het antwoord '42' geeft de uitvoer 'Ja'"""
    args = "42"
    target = "Ja"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def checks_answer1(test):
    """het antwoord 'tweeenveertig' geeft de uitvoer 'Ja'"""
    args = "tweeenveertig"
    target = "Ja"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def checks_answer2(test):
    """het antwoord 'tweeënveertig' geeft de uitvoer 'Ja'"""
    args = "tweeënveertig"
    target = "Ja"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(40)
def checks_answer3(test):
    """het antwoord '53' geeft de uitvoer 'Nee'"""
    args = "53"
    target = "Nee"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)
    test.test = testMethod
