import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics_no_listcomp import *
from _static_analysis import *

# special check in has_functions because of older assignment version
from checkpy import static

@t.passed(doctest_ok)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert defines_function("check_coin")
    assert defines_function("determine_due")
    if "prompt_coin" in static.getFunctionDefinitions():
        raise AssertionError("`prompt_coin` is aanwezig, maar dat staat niet in de opdracht")
    assert in_code(ast.While)
    assert not_in_code(ast.For)
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)

@t.passed(doctest_ok)
@t.test(10)
def checks_coin(test):
    """functie `check_coin` werkt correct"""
    def testMethod():
        coin = lib.getFunction("check_coin", test.fileName)
        if coin(25) and coin(10) and coin(5) and not coin(1) and not coin("10"):
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
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

@t.passed(doctest_ok)
@t.test(30)
def checks_main(test):
    """wisselgeld van 10 cent wordt verkregen na invoeren van 25, 10, en dan 25 cent"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=[25, 10, 25],
            overwriteAttributes = [("__name__", "__main__")])
        answer = "10"
        return asserts.exact(output.strip()[-2:], answer)
    test.test = testMethod
