import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics_no_listcomp import *
from _static_analysis import *

@t.passed(doctest_ok)
def has_functions():
    """functie `convert` is aanwezig"""
    assert defines_function("convert")

@t.passed(has_functions)
@t.test(9)
def checks_no_index(test):
    """oplossing gebruikt geen `.index()` of `.find()`"""
    def testMethod():
        if has_string(".index") or has_string(".find"):
            return False, "gebruik geen .index() of .find() voor deze opdracht"
        return True
    test.test = testMethod

@t.passed(has_functions)
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

@t.passed(has_functions)
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

@t.passed(has_functions)
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
