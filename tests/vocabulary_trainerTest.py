from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, mypy_strict, doctest
# forbidden_constructs.disallow_all()

@passed(checkstyle, mypy_strict, doctest)
def test_class():
    """class `VocabularyTrainer` is aanwezig"""
    VocabularyTrainer = getModule().VocabularyTrainer
    assert VocabularyTrainer()

@passed(test_class)
def test_add_and_get():
    """"""
    VocabularyTrainer = getModule().VocabularyTrainer
    vt = VocabularyTrainer()
    vt.add_word("huis", "house")
    assert vt.get_translation("huis") == ["house"]

@passed(test_class)
def test_add_duplicates():
    """"""
    VocabularyTrainer = getModule().VocabularyTrainer
    vt = VocabularyTrainer()
    vt.add_word("huis", "house")
    vt.add_word("huis", "home")
    # order doesn't matter
    assert set(vt.get_translation("huis")) == {"house", "home"}

@passed(test_class)
def test_remove():
    """"""
    VocabularyTrainer = getModule().VocabularyTrainer
    vt = VocabularyTrainer()
    vt.add_word("boom", "tree")
    vt.remove_word("boom")
    assert vt.get_translation("boom") == None

@passed(test_class)
def test_list_words():
    """"""
    VocabularyTrainer = getModule().VocabularyTrainer
    vt = VocabularyTrainer()
    vt.add_word("a", "1")
    vt.add_word("b", "2")
    assert set(vt.list_words()) == {"a", "b"}
