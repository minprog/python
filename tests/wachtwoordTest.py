import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.test(10)
def checks_length(test):
    def testMethod():
        length = lib.getFunction("check_length", test.fileName)
        if length("12345678") and length("ThisIsAtLeast8") and not length("") and not length("1234567"):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "check_length"


@t.test(20)
def checks_letter(test):
    def testMethod():
        letter = lib.getFunction("check_letter", test.fileName)
        if letter("AaBbCc") and not letter("abc") and not letter("ABC") and not letter("123"):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "check_letter"


@t.test(30)
def checks_number(test):
    def testMethod():
        number = lib.getFunction("check_number", test.fileName)
        if number("123") and number("Hello123") and not number("Hello") and number("1") and number("2") and number("3") and number("4") and number("5") and number("6") and number("7") and number("8") and number("9") and number("0"):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "check_number"

@t.test(40)
def checks_password(test):
    def testMethod():
        password = lib.getFunction("check_password", test.fileName)
        if password("AardappelTester123") and not password("hoi") and not password("Practitioner") and not password("Arb1ter") and not password("shopkeeper") and not password("12345678") and not password("1234"):
            return True
        else:
            return False

    test.test = testMethod
    test.description = lambda : "check_password"

@t.test(50)
def check_any(test):
    def testMethod():
        source_no_comments = lib.removeComments(lib.source(test.fileName))
        return "any(" not in source_no_comments and "any (" not in source_no_comments
    test.test = testMethod
    test.description = lambda : "programma gebruikt niet any()"
