import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics_no_listcomp import *

@t.passed(doctest_ok)
@t.test(9)
def check_code(test):
    """wel loops gebruikt in deze opdracht"""
    assert in_code(ast.For)
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@t.passed(check_code)
def has_functions():
    """functies `check_length` enz. zijn aanwezig"""
    assert defines_function("check_length")
    assert defines_function("check_letter")
    assert defines_function("check_number")
    assert defines_function("check_password")

@t.passed(has_functions)
@t.test(10)
def checks_length(test):
    """functie `check_length` werkt correct"""
    def testMethod():
        length = lib.getFunction("check_length", test.fileName)
        if length("12345678") and length("ThisIsAtLeast8") and not length("") and not length("1234567"):
            return True
        else:
            return False
    test.test = testMethod

@t.passed(has_functions)
@t.test(20)
def checks_letter(test):
    """functie `check_letter` werkt correct"""
    def testMethod():
        letter = lib.getFunction("check_letter", test.fileName)
        if letter("AaBbCc") and not letter("abc") and not letter("ABC") and not letter("123"):
            return True
        else:
            return False
    test.test = testMethod

@t.passed(has_functions)
@t.test(30)
def checks_number(test):
    """functie `check_number` werkt correct"""
    def testMethod():
        number = lib.getFunction("check_number", test.fileName)
        if number("123") and number("Hello123") and not number("Hello") and number("1") and number("2") and number("3") and number("4") and number("5") and number("6") and number("7") and number("8") and number("9") and number("0"):
            return True
        else:
            return False
    test.test = testMethod

@t.passed(has_functions)
@t.test(40)
def checks_password(test):
    """functie `check_password` werkt correct"""
    def testMethod():
        password = lib.getFunction("check_password", test.fileName)
        if password("AardappelTester123") and not password("hoi") and not password("Practitioner") and not password("Arb1ter") and not password("shopkeeper") and not password("12345678") and not password("1234"):
            return True
        else:
            return False
    test.test = testMethod
