import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

def expectedOutput(target, args):
    return f"het antwoord '{args}' geeft de uitvoer '{target}'"

@t.test(10)
def checks_answer0(test):
    args = "42"
    target = "Ja"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(20)
def checks_answer1(test):
    args = "tweeenveertig"
    target = "Ja"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

@t.test(30)
def checks_answer2(test):
    args = "tweeënveertig"
    target = "Ja"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)

# uitgecomment want dit staat niet in de opdracht, plus de string-methods
# zijn nog niet behandeld in week 1
# @t.test(4)
# def checks_answer3(test):
#     args = "TWEEENVEERTIG"
#     target = "Ja"
#     def testMethod():
#         output = lib.outputOf(test.fileName, stdinArgs=[args],
#                     overwriteAttributes = [("__name__", "__main__")])
#         return asserts.exact(output.strip().split('\n')[-1], target)
#
#     test.test = testMethod
#     test.description = lambda : expectedOutput(target, args)

@t.test(50)
def checks_answer4(test):
    args = "53"
    target = "Nee"
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[args],
                    overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip().split('\n')[-1], target)

    test.test = testMethod
    test.description = lambda : expectedOutput(target, args)
