import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.passed(doctest_ok)
@t.test(10)
def checks_calculate_years(test):
    """functie 'calculate_years' werkt correct"""
    def testMethod():
        calculate_years = lib.getFunction("calculate_years", test.fileName)
        if (calculate_years(1200, 1300) == 1 and calculate_years(20, 100) == 20
            and calculate_years(100, 1000000) == 115 and calculate_years(50, 600) == 32):
            return True
        else:

            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def check_overall2(test):
    """kan overweg met foute invoer"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[6, 9, 5, -6, 18],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), "8")
    test.test = testMethod
