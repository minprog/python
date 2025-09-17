from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
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

@passed(has_functions)
def test_function(test):
    """functie `check_input` werkt correct"""
    check_input = getFunction("check_input")
    assert_return(True , check_input, "ATGC")
    assert_return(True , check_input, "agtc")
    assert_return(False, check_input, "AUGA")
    assert_return(False, check_input, "123")

@passed(has_functions)
def test_function2(test):
    """functie `transcribe_dna_to_rna` werkt correct met elke combinatie van uppercase/lowercase"""
    transcribe_dna_to_rna = getFunction("transcribe_dna_to_rna")
    assert_return("UACG", transcribe_dna_to_rna, "ATGC")
    assert_return("UUACG", transcribe_dna_to_rna, "aatgc")

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(run('ATGC'), "RNA: UACG\n")
    assert_output(run('atGcAgtAttGCA'), "RNA: UACGUCAUAACGU\n")
    assert_output(run('hello'), "That is not a valid DNA string\n")
