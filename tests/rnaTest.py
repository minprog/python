import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics_no_listcomp import *
from _static_analysis import *

@t.passed(doctest_ok)
def has_functions():
    """functie `check_input` enz. zijn aanwezig"""
    assert defines_function("check_input")
    assert defines_function("transcribe_dna_to_rna")
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@t.passed(has_functions)
@t.test(10)
def checks_input(test):
    """functie `check_input` werkt correct"""
    def testMethod():
        input_dna = lib.getFunction("check_input", test.fileName)
        if (
            input_dna("ATGC")
            and input_dna("agtc")
            and not input_dna("AUGA")
            and not input_dna("123")
        ):
            return True
        else:
            return False
    test.test = testMethod

@t.passed(has_functions)
@t.test(20)
def checks_convert_dna(test):
    """functie `transcribe_dna_to_rna` werkt correct met elke combinatie van uppercase/lowercase"""
    def testMethod():
        if has_string(".index"):
            return False, "gebruik geen .index() voor deze opdracht"

        convert = lib.getFunction("transcribe_dna_to_rna", test.fileName)
        return (convert("ATGC") == "UACG" and convert("aatgc") == "UUACG")
    test.test = testMethod
