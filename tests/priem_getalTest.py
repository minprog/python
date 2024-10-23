from _basics_no_listcomp import *

@t.passed(doctest_ok)
def has_function_1():
    """functie `is_priem` is aanwezig"""
    assert defines_function("is_priem")

@t.passed(has_function_1)
def test_function_1(test):
    """functie `is_priem` werkt correct"""
    assert getFunction("is_priem")(1) == False
    assert getFunction("is_priem")(2) == True
    assert getFunction("is_priem")(7919) == True
    assert getFunction("is_priem")(7920) == False

@t.passed(doctest_ok)
def has_function_2():
    """functie `print_priemen_tot` is aanwezig"""
    assert defines_function("print_priemen_tot")

@t.passed(doctest_ok)
def has_function_3():
    """functie `zoveelste_priem` is aanwezig"""
    assert defines_function("zoveelste_priem")

@t.passed(has_function_3)
def test_function_3(test):
    """functie `zoveelste_priem` werkt correct"""
    assert getFunction("zoveelste_priem")(1) == 2
    assert getFunction("zoveelste_priem")(2) == 3
    assert getFunction("zoveelste_priem")(1000) == 7919
    assert getFunction("zoveelste_priem")(377) == 2591

@t.passed(has_function_3)
def test_program(test):
    """vindt het 377e en 1000e priemgetal via input"""
    assert outputOf(stdinArgs=[1000], overwriteAttributes=[("__name__", "__main__")]) == "7919\n"
    assert outputOf(stdinArgs=[377], overwriteAttributes=[("__name__", "__main__")]) == "2591\n"
