from checkpy import *

import sys
import pathlib
sys.path.append(str(pathlib.Path(__file__).parent.parent))
from _basics import *

includeFromTests("dictionary.txt")

#@passed(basic_style, mypy_ok, doctest_ok)
@test()
def canImport():
    """hangman.py loads without printing anything"""
    assert outputOf() == "", "make sure you do not edit the distribution code and make sure your code is free of exceptions"

@passed(canImport, hide=False)
def testLoadLexicon():
    """lexicon object with 4-letter words can be created"""
    hangman = getModule()

    if not hasattr(hangman, "Lexicon"):
        raise AssertionError("missing class 'Lexicon' in hangman.py")

    hangman.Lexicon(4)

@passed(testLoadLexicon, hide=False)
def testLexicon():
    """lexicon object correctly extracts 4-letter words from dictionary.txt"""
    lex = getModule().Lexicon(4)
    
    assert lex.get_word() == Type(str)
    assert len(lex.get_word()) == 4

    if len({lex.get_word() for _ in range(10)}) == 1:
        raise AssertionError("retrieved words are not random, Lexicon.get_word() retrieves the same word each time")

@passed(testLexicon, hide=False)
def testLoadHangman():
    """can create a hangman game with "hello" and 5 guesses"""
    hangman = getModule()

    if not hasattr(hangman, "Hangman"):
        raise AssertionError("missing class 'Hangman' in hangman.py")
    
    try:
        hangman.Hangman("hello", 5)
    except:
        raise AssertionError(
            'This check failed. To reproduce its results run the following in the terminal:\n'
            'python3 -i hangman.py\n'
            '>>> Hangman("hello", 5)'
        )
    
@passed(testLoadHangman, hide=False)
def testGuessesLeftStart():
    """guesses_left() returns the correct number of starting guesses"""
    assert getModule().Hangman("hello", 5).guesses_left() == 5
    assert getModule().Hangman("seven", 7).guesses_left() == 7
    
@passed(testGuessesLeftStart, hide=False)
def testGuessesLeft():
    """calling guesses_left() twice returns the same result"""
    game = getModule().Hangman("hello", 5)

    if game.guesses_left() != game.guesses_left():
        raise AssertionError(
            'This check failed. To reproduce its results run the following in the terminal:\n'
            'python3 -i hangman.py\n'
            '>>> game = Hangman("hello", 5)\n'
            '>>> game.guesses_left()\n'
            '>>> game.guesses_left()'
        )
    
@passed(testGuessesLeft, hide=False)
def testGuess():
    """guess() returns True if letter is in the word, False if not"""
    assert getModule().Hangman("abc", 5).guess("a") == True
    assert getModule().Hangman("abc", 5).guess("d") == False

@passed(testGuess, hide=False)
def testGuessRepeatedLetter():
    """guess() returns True if letter is in the word, then False when that same letter is guessed again"""
    game = getModule().Hangman("abc", 5)
    
    if not game.guess("a") or game.guess("a"):
        raise AssertionError(
            'This check failed. To reproduce its results run the following in the terminal:\n'
            'python3 -i hangman.py\n'
            '>>> game = Hangman("abc", 5)\n'
            '>>> game.guess("a")\n'
            '>>> game.guess("a")'
        )
    
@passed(testGuessRepeatedLetter, hide=False)
def testGuessesDecreaseAfterGuess():
    """guesses_left() decreases after a call to guess()"""
    game = getModule().Hangman("abc", 5)

    start = game.guesses_left()
    game.guess("a")
    end = game.guesses_left()

    if start != end + 1:
        raise AssertionError(
            'This check failed. To reproduce its results run the following in the terminal:\n'
            'python3 -i hangman.py\n'
            '>>> game = Hangman("abc", 5)\n'
            '>>> game.guesses_left()\n'
            '>>> game.guess("a")\n'
            '>>> game.guesses_left()'
        )