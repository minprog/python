from checkpy import *
from _static_analysis import *

# TODO modernize
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("calculate_years")

    assert in_code(ast.While)
    assert not_in_code(ast.For)
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)


@passed(has_functions)
@test(10)
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

@passed(has_functions)
@test(20)
def check_overall2(test):
    """kan overweg met foute invoer"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[6, 9, 5, -6, 18],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.contains(output.strip(), "8")
    test.test = testMethod
