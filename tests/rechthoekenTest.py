from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def has_functions():
    """functie `is_same_rectangle` is aanwezig"""
    assert function_defined_in_module("is_same_rectangle")

@passed(has_functions)
def check_is_same_rectangle(test):
    """functie `is_same_rectangle` werkt correct"""
    is_same_rectangle = get_function("is_same_rectangle")
    assert is_same_rectangle(1,2,3,4) == False
    assert is_same_rectangle(1,2,1,2) == True

@passed(has_functions)
def check_is_same_square(test):
    """functie `is_same_square` werkt correct"""
    is_same_square = get_function("is_same_square")
    assert is_same_square(1,2,1,2) == False
    assert is_same_square(1,1,2,2) == False
    assert is_same_square(1,1,1,1) == True
    assert is_same_square(2,2,2,2) == True

@passed(has_functions)
def check_calculate_length(test):
    """functie `calculate_length` werkt correct"""
    calculate_length = get_function("calculate_length")
    assert calculate_length(-2,  2) == 4
    assert calculate_length( 2, -2) == 4
    assert calculate_length( 0,  4) == 4
    assert calculate_length( 4,  0) == 4
    assert calculate_length( 3,  9) == 6

@passed(has_functions)
def check_identical_rectangle(test):
    """het programma identificeert gelijke rechthoeken"""

    input_entries = ["0", "7", "0", "4", "6", "13", "2", "6"]
    target_1 = ['zijn gelijk!', 'are identical!']
    target_2 = ['vierkant!', ' square,']
    target_3 = ['niks aan', 'to report']

    output = run(*input_entries).strip()

    if not any([target in output for target in target_1]):
        raise AssertionError(f"verwachtte iets van gelijke rechthoeken voor {','.join(input_entries)}")

    if any([target in output for target in target_3]):
        raise AssertionError(f"verwachtte geen gelijke rechthoeken voor {','.join(input_entries)}")

@passed(has_functions)
def check_identical_square(test):
    """het programma identificeert gelijke vierkanten"""

    input_entries = ["0", "7", "0", "7", "6", "13", "2", "9"]
    target_1 = ['zijn gelijk!', 'are identical!']
    target_2 = ['vierkant!', ' square,']
    target_3 = ['niks aan', 'to report']

    output = run(*input_entries).strip()

    # TODO volgorde van rechthoek/vierkant is niet gegarandeerd

    if not any([target in output for target in target_1]):
        raise AssertionError(f"verwachtte iets van gelijke rechthoeken voor {','.join(input_entries)}")

    if not any([target in output for target in target_2]):
        raise AssertionError(f"verwachtte iets van gelijke vierkanten voor {','.join(input_entries)}")

@passed(has_functions)
def check_no_result(test):
    """het programma rapporteert teleurstelling bij gebrek aan gelijkheid"""

    input_entries = ["0", "7", "0", "7", "6", "15", "2", "9"]
    target_1 = ['zijn gelijk!', 'are identical!']
    target_2 = ['vierkant!', ' square,']
    target_3 = ['niks aan', 'to report']

    output = run(*input_entries).strip()

    if not any([target in output for target in target_3]):
        raise AssertionError(f"verwachtte iets van 'niks aan' voor {','.join(input_entries)}")
    if any([target in output for target in target_1]):
        raise AssertionError(f"verwachtte geen 'niks aan' voor {','.join(input_entries)}")
    if any([target in output for target in target_2]):
        raise AssertionError(f"verwachtte geen 'niks aan' voor {','.join(input_entries)}")
