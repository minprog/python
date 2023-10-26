import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics_no_listcomp import *

@t.passed(doctest_ok)
@t.test(10)
def calculatesZeroCaffeine(test):
    """print 'Je krijgt 0 mg cafeine binnen.' bij [0, 0, 0, 0] als invoer"""
    args = [0, 0, 0, 0]
    target = "0 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def calculatesCoffee(test):
    """print 'Je krijgt 90 mg cafeine binnen.' bij [1, 0, 0, 0] als invoer"""
    args = [1, 0, 0, 0]
    target = "90 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def calculatesTea(test):
    """print 'Je krijgt 45 mg cafeine binnen.' bij [0, 1, 0, 0] als invoer"""
    args = [0, 1, 0, 0]
    target = "45 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def calculatesEnergy(test):
    """print 'Je krijgt 80 mg cafeine binnen.' bij [0, 0, 1, 0] als invoer"""
    args = [0, 0, 1, 0]
    target = "80 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def calculatesCola(test):
    """print 'Je krijgt 40 mg cafeine binnen.' bij [0, 0, 0, 1] als invoer"""
    args = [0, 0, 0, 1]
    target = "40 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def calculatesSomeCafeine(test):
    """print 'Je krijgt 580 mg cafeine binnen.' bij [1, 2, 3, 4] als invoer"""
    args = [1, 2, 3, 4]
    target = "580 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)
    test.test = testMethod
