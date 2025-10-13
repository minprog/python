from checkpy import *
from _pyprog_tools import *
from _list_tracking import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(forbidden_constructs)
def has_function_split_by_parity():
    """functie `split_by_parity` is aanwezig"""
    assert function_defined_in_module("split_by_parity")

@passed(has_function_split_by_parity)
def test_split_by_parity(test):
    """functie `split_by_parity` werkt correct"""
    split_by_parity = get_function("split_by_parity")
    assert no_input_output_in_function(split_by_parity)
    assert split_by_parity([1, 2, 3, 4]) == [[2, 4], [1, 3]]

    arg1 = HistoryList([1, 2, 3, 4])
    result = split_by_parity(arg1)
    if len(arg1.history) > 1:
        raise AssertionError("de gegeven lijst is aangepast, dit mag niet")

    assert split_by_parity([1, 3, 2, 4]) == [[2, 4], [1, 3]]
    assert split_by_parity([3, 2, 4]) == [[2, 4], [3]]
    assert split_by_parity([2, 4]) == [[2, 4], []]
    assert split_by_parity([1, 3, 4]) == [[4], [1, 3]]
    assert split_by_parity([1, 3]) == [[], [1, 3]]
    assert split_by_parity([1]) == [[], [1]]
    assert split_by_parity([]) == [[], []]

@passed(forbidden_constructs)
def has_function_reading_level():
    """functie `reading_level` is aanwezig"""
    assert function_defined_in_module("reading_level")

@passed(has_function_reading_level)
def test_reading_level(test):
    """functie `reading_level` werkt correct"""
    reading_level = get_function("reading_level")
    assert no_input_output_in_function(reading_level)
    assert reading_level("Mijn naam is Pim") == 9.75
    assert reading_level("mma") == 3.0
    assert reading_level("Mma") == 3.0

@passed(forbidden_constructs)
def has_function_longest_word_length():
    """functie `longest_word_length` is aanwezig"""
    assert function_defined_in_module("longest_word_length", "longest_word_lenght")
    if string_in_module(".split("):
        raise AssertionError("je mag geen .split() gebruiken bij de toets")

@passed(has_function_longest_word_length)
def test_longest_word_length(test):
    """functie `longest_word_length` werkt correct"""
    longest_word_length = get_function("longest_word_length", "longest_word_lenght")
    assert no_input_output_in_function(longest_word_length)
    assert longest_word_length("mijn naam is pim") == 4
    assert longest_word_length("mma") == 3
    assert longest_word_length("lahetetty joensuun hotellista") == 10

@passed(forbidden_constructs)
def has_function_encrypt():
    """functie `encrypt` is aanwezig"""
    assert function_defined_in_module("encrypt")

@passed(has_function_encrypt)
def test_encrypt(test):
    """functie `encrypt` werkt correct"""
    encrypt = get_function("encrypt")
    assert no_input_output_in_function(encrypt)
    assert encrypt("abc") == 'zyx'
    assert encrypt("zyx") == 'abc'
    assert encrypt('') == ''
    assert encrypt('helloworld') == 'svooldliow'

@passed(forbidden_constructs)
def has_function_vowely_words():
    """functie `vowely_words` is aanwezig"""
    assert function_defined_in_module("vowely_words")

class SafeString(str):
    def lower(self):
        raise AssertionError("je mag geen lower gebruiken voor de hele string!")

    def upper(self):
        raise AssertionError("je mag geen upper gebruiken voor de hele string!")

@passed(has_function_vowely_words)
def test_vowely_words(test):
    """functie `vowely_words` werkt correct"""
    vowely_words = get_function("vowely_words")
    assert no_input_output_in_function(vowely_words)
    assert vowely_words([SafeString("Aap")]) == ['Aap']
    assert vowely_words(['Aap', 'Noot', 'Mies']) == ['Aap', 'Noot', 'Mies']
    assert vowely_words(['de', 'het', 'een']) == ['een']
    assert vowely_words(['De']) == []
    assert vowely_words(['Rookgordijn']) == ['Rookgordijn']
    assert vowely_words(['open']) == ['open']
    assert vowely_words([]) == []
