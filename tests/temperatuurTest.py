import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.test(10)
def checks_convert_temperature(test):
    def testMethod():
        convert_temperature = lib.getFunction("convert_temperature", test.fileName)
        if convert_temperature("C", 10) == 50 and convert_temperature("F", 9) == -12:
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "'convert_temperature' works correctly."


# @t.test(1)
# def checks_capital(test):
#     def testMethod():
#         convert_temperature = lib.getFunction("convert_temperature", test.fileName)
#         if (convert_temperature("C", 10) and convert_temperature("c", 10) and
#             convert_temperature("F", 9) and convert_temperature("f", 9)):
#             return True
#         else:
#             return False
#
#     test.test = testMethod
#     test.description = lambda : "All of 'C', 'F', 'c' and 'f' are accepted by the program."


@t.test(20)
def check_overall1(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["F", 0, 9, 3],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "F |   C\n  0 | -17\n  3 | -16\n  6 | -14\n  9 | -12")

    test.test = testMethod
    test.description = lambda : "The correct table is printed when converting F to C with 0 as begin temperature, 9 as end temperature and 3 as step size."


@t.test(30)
def check_overall2(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["C", 0, 20, 5],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "C |   F\n  0 |  32\n  5 |  41\n 10 |  50\n 15 |  59\n 20 |  68")

    test.test = testMethod      
    test.description = lambda : "The correct table is printed when converting C to F with 0 as begin temperature, 20 as end temperature and 5 as step size."

@t.test(40)
def check_overall3(test):
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["f", 0, 9, 3],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "F |   C\n  0 | -17\n  3 | -16\n  6 | -14\n  9 | -12")

    test.test = testMethod
    test.description = lambda : "The correct table is printed when converting f (lowercase) to C with 0 as begin temperature, 9 as end temperature and 3 as step size."
