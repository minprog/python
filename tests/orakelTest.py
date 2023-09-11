import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

def expectedOutput(target, args):
    return f"het antwoord '{args}' geeft de uitvoer '{target}'"

@t.test(1)
def checks_answer0(test):
    args = "42"
    target = "Ja"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(2)
def checks_answer1(test):
    args = "tweeenveertig"
    target = "Ja"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(3)
def checks_answer2(test):
    args = "tweeënveertig"
    target = "Ja"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(4)
def checks_answer3(test):
    args = "TWEEENVEERTIG"
    target = "Ja"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(5)
def checks_answer4(test):
    args = "53"
    target = "Nee"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)
