from _basics_no_listcomp import *

@t.passed(doctest_ok)
def has_function_1():
    """functie `is_priem` is NIET aanwezig"""
    assert not_defines_function("is_priem")

@t.passed(doctest_ok)
def has_function_2():
    """functie `zoek_langste_reeks` is aanwezig"""
    assert defines_function("zoek_langste_reeks")

@t.passed(has_function_2)
def test_function_3(test):
    """functie `zoek_langste_reeks` werkt correct"""
    assert getFunction("zoek_langste_reeks")(10000) == (9552, 9586)
    assert getFunction("zoek_langste_reeks")(100) == (90, 96)

@t.passed(doctest_ok)
def has_function_3():
    """functie `print_boodschap` is aanwezig"""
    assert defines_function("print_boodschap")
