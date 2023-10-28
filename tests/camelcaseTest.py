import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics_no_listcomp import *
from _static_analysis import *

@t.passed(doctest_ok)
@t.test(9)
def checks_no_index(test):
    """oplossing gebruikt geen `.index()`"""
    def testMethod():
        if has_string(".index"):
            return False, "gebruik geen .index() voor deze opdracht"
        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(10)
def checks_convert0(test):
    """aanroep `convert('check')` geeft `check`"""
    def testMethod():
        convert = lib.getFunction("convert", test.fileName)
        if convert("check") == "check":
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def checks_convert1(test):
    """aanroep `convert('convertInput')` geeft `convert_input`"""
    def testMethod():
        convert = lib.getFunction("convert", test.fileName)
        if convert("convertInput") == "convert_input":
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def checks_convert2(test):
    """aanroep `convert('readFromFile')` geeft `read_from_file`"""
    def testMethod():
        convert = lib.getFunction("convert", test.fileName)
        if convert("readFromFile") == "read_from_file":
            return True
        else:
            return False
    test.test = testMethod
