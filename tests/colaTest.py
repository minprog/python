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
    assert defines_function("check_coin")
    assert defines_function("determine_due")

    assert in_code(ast.While)
    assert not_in_code(ast.For)
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_in_code(ast.In)

@passed(has_functions)
@test(10)
def checks_coin(test):
    """functie `check_coin` werkt correct"""
    def testMethod():
        coin = lib.getFunction("check_coin", test.fileName)
        if coin(25) and coin(10) and coin(5) and not coin(1) and not coin("10"):
            return True
        else:
            return False
    test.test = testMethod

@passed(has_functions)
@test(20)
def checks_due(test):
    """functie `determine_due` werkt correct"""
    def testMethod():
        due = lib.getFunction("determine_due", test.fileName)
        if due(50, 20) == 30:
            return False, "functie accepteert een munt van 20 cent, maar deze bestaat niet"
        if due(50, 25) == 25 and due(50, 20) == 50 and due(50, 10) == 40:
            return True
        else:
            return False
    test.test = testMethod

@passed(has_functions)
@test(30)
def checks_main(test):
    """wisselgeld van 10 cent wordt verkregen na invoeren van 25, 10, en dan 25 cent"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[25, 10, 25],
            overwriteAttributes = [("__name__", "__main__")])
        answer = "10"
        return asserts.exact(output.strip()[-2:], answer)
    test.test = testMethod
