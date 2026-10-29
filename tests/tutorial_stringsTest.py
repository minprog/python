from checkpy import *
from _pyprog_tools import *

from _check_doctests import check_doctests

import _catch_syntax_error
from _catch_syntax_error import no_syntax_error
_catch_syntax_error.MAX_SYNTAX_ERRORS = 2

def defined(name):
    assert function_defined_in_module(name)
    return get_function(name)

@test()
def test_greet():
    """functie `greet` werkt correct"""
    assert defined("greet")() == "Hello"

@test()
def test_first_char():
    """functie `first_char` werkt correct"""
    f = defined("first_char")
    assert f("Python") == "P"
    assert f("abc") == "a"

@test()
def test_last_char():
    """functie `last_char` werkt correct"""
    f = defined("last_char")
    assert f("Python") == "n"
    assert f("code") == "e"

@test()
def test_excited():
    """functie `excited` werkt correct"""
    f = defined("excited")
    assert f("Hi") == "Hi!!!"
    assert f("You") == "You!!!"

@test()
def test_double_and_space():
    """functie `double_and_space` werkt correct"""
    f = defined("double_and_space")
    assert f("go", "team") == "gogo teamteam"
    assert f("a", "b") == "aa bb"

@test()
def test_part_of_python():
    """functie `part_of_python` werkt correct"""
    f = defined("part_of_python")
    assert f("py").is_(True)
    assert f("n").is_(True)
    assert f("java").is_(False)

@test()
def test_has_o():
    """functie `has_o` werkt correct"""
    f = defined("has_o")
    assert f("dog").is_(True)
    assert f("cat").is_(False)

@test()
def test_has_no_o():
    """functie `has_no_o` werkt correct"""
    f = defined("has_no_o")
    assert f("cat").is_(True)
    assert f("dog").is_(False)

@test()
def test_where_o_at():
    """functie `where_o_at` werkt correct"""
    f = defined("where_o_at")
    assert f("Python") == 4
    assert f("abc") == -1
    assert f("ooo") == 0

@test()
def test_shout():
    """functie `shout` werkt correct"""
    f = defined("shout")
    assert f("hello") == "HELLO!"

@test()
def test_quiet():
    """functie `quiet` werkt correct"""
    f = defined("quiet")
    assert f("LOUD") == "loud..."

@test()
def test_count_vowels():
    """functie `count_vowels` werkt correct"""
    f = defined("count_vowels")
    assert f("education") == 5
    assert f("Python") == 1
    assert f("RODENT!") == 2
    assert f("") == 0

@test()
def test_isspace():
    """functie `isspace` werkt correct"""
    f = defined("isspace")
    assert f(" ").is_(True)
    assert f("\t").is_(True)
    assert f("\n").is_(True)
    assert f("\\n").is_(False)
    assert f("a").is_(False)
    assert f("space").is_(False)
    assert f("").is_(False)

@test()
def test_isvowel():
    """functie `isvowel` werkt correct"""
    f = defined("isvowel")
    for v in "aeiou":
        assert f(v).is_(True)
    assert f("y").is_(False)
    assert f("aa").is_(True)
    assert f("aeiou").is_(True)
    assert f("slim").is_(False)
    assert f("imma").is_(False)
    assert f("A").is_(False)
    assert f("").is_(True)

@test()
def test_has_single_vowel():
    """functie `has_single_vowel` werkt correct"""
    f = defined("has_single_vowel")
    assert f("a").is_(True)
    assert f("bims").is_(True)
    assert f("smib").is_(True)
    assert f("y").is_(False)
    assert f("yolo").is_(False)
    assert f("rough").is_(False)
    assert f("").is_(False)

@test()
def test_is_different():
    """functie `is_different` werkt correct"""
    f = defined("is_different")
    assert f("dance", "night").is_(True)
    assert f("dance", "dance").is_(False)
    assert f("a", "e").is_(True)
    assert f("A", "a").is_(True)
    assert f("piano", "pianissimo").is_(True)
    assert f("", "mamba").is_(True)
    assert f("mamba", "").is_(True)
    assert f("", "").is_(False)

@test()
def test_count_difference():
    """functie `count_difference` werkt correct"""
    f = defined("count_difference")
    assert f("dance", "night") == 5
    assert f("dance", "dance") == 0
    assert f("a", "e") == 1
    assert f("A", "a") == 1
    assert f("jumpstyle", "hakken") == 9
    assert f("piano", "pianissimo") == 6
    assert f("", "mamba") == 5
    assert f("mamba", "") == 5
    assert f("", "") == 0

@test(100)
def doctests(test):
    """elke functie heeft voldoende doctests en ze geven allemaal akkoord"""
    def testMethod():
        return check_doctests(test, True)
    test.test = testMethod
    test.fail = lambda info: info
    test.timeout = lambda: 120
