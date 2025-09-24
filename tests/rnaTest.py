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
    check_input = get_function("check_input")
    assert check_input("ATGC") == True
    assert check_input("agtc") == True
    assert check_input("AUGA") == False
    assert check_input("123") == False

@passed(has_functions)
def test_function2(test):
    """functie `transcribe_dna_to_rna` werkt correct met elke combinatie van uppercase/lowercase"""
    transcribe_dna_to_rna = get_function("transcribe_dna_to_rna")
    assert transcribe_dna_to_rna("ATGC") == "UACG"
    assert transcribe_dna_to_rna("aatgc") == "UUACG"

@passed(has_functions)
def test_program(test):
    """het programma werkt correct met invoer en uitvoer"""
    assert_output(run('ATGC'), "RNA: UACG\n")
    assert_output(run('atGcAgtAttGCA'), "RNA: UACGUCAUAACGU\n")
    assert_output(run('hello'), "That is not a valid DNA string\n")
