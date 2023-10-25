import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.passed(doctest_ok)
@t.test(10)
def checks_answer0(test):
    """3 + 5 = 8.0"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["3 + 5"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "8.0")
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def checks_answer1(test):
    """19 - 6 = 13.0"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["19 - 6"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "13.0")
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def checks_answer2(test):
    """6 - 19 = -13.0"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["6 - 19"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "-13.0")
    test.test = testMethod


@t.passed(doctest_ok)
@t.test(40)
def checks_answer3(test):
    """12 * 23 = 276.0"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["12 * 23"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "276.0")
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(50)
def checks_answer4(test):
    """6 / 4 = 1.5"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["6 / 4"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "1.5")
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(60)
def checks_answer5(test):
    """-8 * 12 = -96.0"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["-8 * 12"],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "-96.0")
    test.test = testMethod
