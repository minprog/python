from checkpy import *
from _static_analysis import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def has_functions():
    """functies `coleman_liau` en `calculate_grade` zijn aanwezig"""
    assert defines_function("coleman_liau")
    assert defines_function("calculate_grade")
    assert in_code(ast.For)
    assert not_in_code(ast.Set)
    assert not_in_code(ast.List)
    assert not_in_code(ast.Tuple)
    assert not_in_code(ast.Dict)
    assert not_has_stringmult()
    assert not_has_stringmethods()

@passed(has_functions)
@test(10)
def checks_coleman_liau(test):
    """functie `coleman_liau` werkt correct"""
    def testMethod():
        coleman_liau = getFunction("coleman_liau", test.fileName)
        if coleman_liau(100, 5, 500) == 12:
            return True
        else:
            return False
    test.test = testMethod

@passed(has_functions)
@test(20)
def checks_calculate_grade(test):
    """functie `calculate_grade` werkt correct"""
    def testMethod():
        calculate_grade = getFunction("calculate_grade", test.fileName)
        if calculate_grade("One fish. Two fish. Red fish. Blue fish.") == -9:
            return True
        else:
            return False
    test.test = testMethod

@passed(has_functions)
@test(30)
def checks_tekst1(test):
    """geeft Grade 7 voor "In my younger and more..." """
    output = outputOf(test.fileName, stdinArgs=["In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since."],
        overwriteAttributes = [("__name__", "__main__")])
    assert output.strip() == "Grade 7", "zorg dat de output exact zo is als in de voorbeelden"

@passed(has_functions)
@test(40)
def checks_tekst2(test):
    """geeft Grade 10 voor "It was a bright cold day..." """
    output = outputOf(test.fileName, stdinArgs=["It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."],
        overwriteAttributes = [("__name__", "__main__")])
    assert output.strip() == "Grade 10"
