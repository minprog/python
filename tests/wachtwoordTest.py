from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
@test(9)
def check_code(test):
    """wel loops gebruikt in deze opdracht"""
    assert construct_in_ast(ast.For)
    assert construct_not_in_ast(ast.Set)
    assert construct_not_in_ast(ast.List)
    assert construct_not_in_ast(ast.Tuple)
    assert construct_not_in_ast(ast.Dict)
    assert no_string_mult_used()
    assert no_string_methods_used()

@passed(check_code)
def has_functions():
    """functies `check_length` enz. zijn aanwezig"""
    assert function_defined_in_module("check_length")
    assert function_defined_in_module("check_letter")
    assert function_defined_in_module("check_number")
    assert function_defined_in_module("check_password")

@passed(has_functions)
@test(10)
def checks_length(test):
    """functie `check_length` werkt correct"""
    def testMethod():
        length = getFunction("check_length", test.fileName)
        if length("12345678") and length("ThisIsAtLeast8") and not length("") and not length("1234567"):
            return True
        else:
            return False
    test.test = testMethod

@passed(has_functions)
@test(20)
def checks_letter(test):
    """functie `check_letter` werkt correct"""
    def testMethod():
        letter = getFunction("check_letter", test.fileName)
        if letter("AaBbCc") and not letter("abc") and not letter("ABC") and not letter("123"):
            return True
        else:
            return False
    test.test = testMethod

@passed(has_functions)
@test(30)
def checks_number(test):
    """functie `check_number` werkt correct"""
    def testMethod():
        number = getFunction("check_number", test.fileName)
        if number("123") and number("Hello123") and not number("Hello") and number("1") and number("2") and number("3") and number("4") and number("5") and number("6") and number("7") and number("8") and number("9") and number("0"):
            return True
        else:
            return False
    test.test = testMethod

@passed(has_functions)
@test(40)
def checks_password(test):
    """functie `check_password` werkt correct"""
    def testMethod():
        password = getFunction("check_password", test.fileName)
        if password("AardappelTester123") and not password("hoi") and not password("Practitioner") and not password("Arb1ter") and not password("shopkeeper") and not password("12345678") and not password("1234"):
            return True
        else:
            return False
    test.test = testMethod
