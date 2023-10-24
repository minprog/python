import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

def expectedOutput(target, args):
    return f"print 'Je krijgt {target} cafeine binnen.' bij {str(args)} als invoer"

@t.test(10)
def calculatesZeroCaffeine(test):
    args = [0, 0, 0, 0]
    target = "0 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(20)
def calculatesCoffee(test):
    args = [1, 0, 0, 0]
    target = "90 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(20)
def calculatesTea(test):
    args = [0, 1, 0, 0]
    target = "45 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(20)
def calculatesEnergy(test):
    args = [0, 0, 1, 0]
    target = "80 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(20)
def calculatesCola(test):
    args = [0, 0, 0, 1]
    target = "40 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(30)
def calculatesSomeCafeine(test):
    args = [1, 2, 3, 4]
    target = "580 mg"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=args,
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)
