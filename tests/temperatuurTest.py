from checkpy import *
from _static_analysis import *

# TODO modernize
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _python_checks import forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()

@passed(has_functions)
@test(10)
def checks_convert_temperature(test):
    """functie 'convert_temperature' werkt correct"""
    def testMethod():
        convert_temperature = lib.getFunction("convert_temperature", test.fileName)
        if convert_temperature("C", 10) == 50 and convert_temperature("F", 9) == -12:
            return True
        else:
            return False
    test.test = testMethod

@passed(has_functions)
@test(20)
def check_overall1(test):
    """print juiste tabel voor F naar C met start 0, eind 9 en stapgrootte 3"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["F", 0, 9, 3],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "F |   C\n  0 | -17\n  3 | -16\n  6 | -14\n  9 | -12")
    test.test = testMethod

@passed(has_functions)
@test(30)
def check_overall2(test):
    """print juiste tabel voor C naar F met start 0, eind 20 en stapgrootte 5"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["C", 0, 20, 5],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "C |   F\n  0 |  32\n  5 |  41\n 10 |  50\n 15 |  59\n 20 |  68")
    test.test = testMethod

@passed(has_functions)
@test(40)
def check_overall3(test):
    """print juiste tabel voor f (lowercase) naar C met start 0, eind 9 en stapgrootte 3"""
    def testMethod():
        output = lib.outputOf(test.fileName, stdinArgs=["f", 0, 9, 3],
            overwriteAttributes = [("__name__", "__main__")])
        return asserts.exact(output.strip(), "F |   C\n  0 | -17\n  3 | -16\n  6 | -14\n  9 | -12")
    test.test = testMethod
