from checkpy import *

import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from _basics import *

includeFromTests("dictionary.txt")

@passed(basic_style, mypy_ok, doctest_ok)
def canImport():
    """hangman.py loads without printing anything"""
    assert outputOf() == "", "make sure you do not edit the distribution code and make sure your code is free of exceptions"

@passed(canImport)
def loadLexicon():
    """lexicon object with 4-letter words can be created"""
    getModule().Lexicon(4)

@passed(loadLexicon)
def testLexicon():
    """lexicon object correctly extracts 4-letter words from dictionary.txt"""
    lex = getModule().Lexicon(4)
    
    assert lex.get_word() == Type(str)

    if len({lex.get_word() for _ in range(10)}) != 10:
        raise AssertionError("retrieved words are not random, Lexicon.get_word() retrieves the same word each time")
