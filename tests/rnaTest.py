import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.passed(doctest_ok)
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

@t.passed(doctest_ok)
@t.test(20)
def checks_convert_dna(test):
    """functie `transcribe_dna_to_rna` werkt correct met elke combinatie van uppercase/lowercase"""
    def testMethod():
        convert = lib.getFunction("transcribe_dna_to_rna", test.fileName)
        if convert(["A", "T", "G", "C"]) == ["U", "A", "C", "G"] and convert(
            ["a", "a", "t", "g", "c"]
        ) == ["U", "U", "A", "C", "G"]:
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def checks_convert_list(test):
    """functie `convert_to_list` werkt correct"""
    def testMethod():
        convert = lib.getFunction("convert_to_list", test.fileName)
        if convert("ATGCAGA") == ["A", "T", "G", "C", "A", "G", "A"]:
            return True
        else:
            return False
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(40)
def checks_convert_string(test):
    """functie `convert_to_string` werkt correct"""
    def testMethod():
        convert = lib.getFunction("convert_to_string", test.fileName)
        if convert(["A", "T", "G", "C", "T", "T", "G"]) == "ATGCTTG":
            return True
        else:
            return False
    test.test = testMethod
