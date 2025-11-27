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
    """één woord toevoegen en dan de vertaling opzoeken"""
    VocabularyTrainer = getModule().VocabularyTrainer
    vt = VocabularyTrainer()
    vt.add_word("huis", "house")
    assert vt.get_translation("huis") in [ {"house"},  ["house"] ]

@passed(test_class)
def test_add_duplicates():
    """twee vertalingen van één woord toevoegen en dan opzoeken"""
    VocabularyTrainer = getModule().VocabularyTrainer
    vt = VocabularyTrainer()
    vt.add_word("huis", "house")
    vt.add_word("huis", "home")
    # order doesn't matter
    assert set(vt.get_translation("huis")) in [ {"house", "home"}, ["house", "home"] ]

@passed(test_class)
def test_remove():
    """één woord toevoegen, dan verwijderen; opzoeken van dat woord geeft een error"""
    VocabularyTrainer = getModule().VocabularyTrainer
    vt = VocabularyTrainer()
    vt.add_word("boom", "tree")
    vt.remove_word("boom")
    raised = False
    try:
        vt.get_translation("boom")
    except KeyError:
        raised = True
    assert raised, "add_contact moet KeyError geven bij duplicate key"

@passed(test_class)
def test_list_words():
    """twee woorden toevoegen; `list_words` moet dan die woorden geven"""
    VocabularyTrainer = getModule().VocabularyTrainer
    vt = VocabularyTrainer()
    vt.add_word("a", "1")
    vt.add_word("b", "2")
    assert vt.list_words() in [ {"a", "b"}, ["a", "b"] ]
