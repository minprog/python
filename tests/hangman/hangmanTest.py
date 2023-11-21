from checkpy import *

import typing
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

    try:
        hangman.Lexicon(4)
    except:
        raiseDebugMessage(
            "Lexicon(4)"
        )

@passed(testLoadLexicon, hide=False)
def testLexicon():
    """lexicon object correctly extracts 4-letter words from dictionary.txt"""
    Lexicon = getModule().Lexicon
    
    try:
        lex = Lexicon(4)
        assert isinstance(lex.get_word(), str)
        assert len(lex.get_word()) == 4
        assert len({lex.get_word() for _ in range(10)}) > 1
    except:
        raiseDebugMessage(
            'lexicon = Lexicon(4)',
            'lexicon.get_word()',
            'lexicon.get_word()',
            'lexicon.get_word()'
        )

@passed(testLexicon, hide=False)
def testLoadHangman():
    """can create a hangman game with "hello" and 5 guesses"""
    hangman = getModule()

    if not hasattr(hangman, "Hangman"):
        raise AssertionError("missing class 'Hangman' in hangman.py")
    
    try:
        hangman.Hangman("hello", 5)
    except:
        raiseDebugMessage(
            'Hangman("hello", 5)'
        )
    
@passed(testLoadHangman, hide=False)
def testGuessesLeftStart():
    """guesses_left() returns the correct number of starting guesses"""
    Hangman = getModule().Hangman
    
    try:
        assert Hangman("hello", 5).guesses_left() == 5
    except:
        raiseDebugMessage(
            'game = Hangman("hello", 5)',
            'game.guesses_left()'
        )

    try:
        assert Hangman("seven", 7).guesses_left() == 7
    except:
        raiseDebugMessage(
            'game = Hangman("seven", 7)',
            'game.guesses_left()'
        )

@passed(testGuessesLeftStart, hide=False)
def testGuessesLeftTwice():
    """calling guesses_left() twice returns the same result"""
    Hangman = getModule().Hangman

    try:
        game = Hangman("hello", 5)
        assert game.guesses_left() == game.guesses_left()
    except:
        raiseDebugMessage(
            'game = Hangman("hello", 5)',
            'game.guesses_left()',
            'game.guesses_left()'
        )
    
@passed(testGuessesLeftTwice, hide=False)
def testGuess():
    """guess() returns True if letter is in the word, False if not"""
    Hangman = getModule().Hangman

    try:
        assert Hangman("abc", 5).guess("a") == True
    except:
        raiseDebugMessage(
            'game = Hangman("abc", 5)',
            'game.guess("a")'
        )

    try:
        assert Hangman("abc", 5).guess("d") == False
    except:
        raiseDebugMessage(
            'game = Hangman("abc", 5)',
            'game.guess("d")'
        )

@passed(testGuess, hide=False)
def testGuessRepeatedLetter():
    """guess() returns True if letter is in the word, then False when that same letter is guessed again"""
    Hangman = getModule().Hangman

    try:
        game = Hangman("abc", 5)
        assert game.guess("a")
        assert not game.guess("a")
    except:
        raiseDebugMessage(
            'game = Hangman("abc", 5)',
            'game.guess("a")',
            'game.guess("a")'
        )
    
@passed(testGuessRepeatedLetter, hide=False)
def testGuessesDecreaseAfterGuess():
    """guesses_left() decreases after a call to guess()"""
    Hangman = getModule().Hangman

    try:
        game = Hangman("abc", 5)
        start = game.guesses_left()
        game.guess("a")
        end = game.guesses_left()
        assert start == end + 1
    except:
        raiseDebugMessage(
            'game = Hangman("abc", 5)',
            'game.guesses_left()',
            'game.guess("a")',
            'game.guesses_left()'
        )
    
@passed(testGuessesDecreaseAfterGuess, hide=False)
def testCurrentPatternEmpty():
    """current_pattern() creates a pattern of underscores of the correct length"""
    Hangman = getModule().Hangman

    try:
        assert Hangman("abc", 5).current_pattern() == "___"
    except:
        raiseDebugMessage(
            'game = Hangman("abc", 5)',
            'game.current_pattern()'
        )
    
    try:
        assert Hangman("hello", 5).current_pattern() == "_____"
    except:
        raiseDebugMessage(
            'game = Hangman("hello", 5)',
            'game.current_pattern()'
        )

@passed(testCurrentPatternEmpty, hide=False)
def testCurrentPatternTwice():
    """calling current_pattern() twice returns the same result"""
    try:
        game = getModule().Hangman("abc", 5)
        assert game.current_pattern() == game.current_pattern()
    except:
        raiseDebugMessage(
            'game = Hangman("abc", 5)',
            'game.current_pattern()',
            'game.current_pattern()'
        )
    
@passed(testCurrentPatternEmpty, hide=False)
def testCurrentPatternChangesAfterGuess():
    """current_pattern() changes after a correct guess"""
    run(
        'game = Hangman("abc", 5)',
        'assert game.current_pattern() == "___"',
        'game.guess("a")',
        'assert game.current_pattern() == "a__"'
    )

    run(
        'game = Hangman("abba", 5)',
        'assert game.current_pattern() == "____"',
        'game.guess("b")',
        'assert game.current_pattern() == "_bb_"'
    )

@passed(testCurrentPatternChangesAfterGuess, hide=False)
def testWonNewGame():
    """won() returns False on a new game"""
    run(
        'game = Hangman("abc", 5)',
        'assert game.won() == False'
    )

def run(*instructions: str):
    """Helper function that 'exec()'s each instruction with shared globals()."""
    env = {}
    exec("from hangman import *", env)
    try:
        for instr in instructions:
            exec(instr, env)
    except:
        raiseDebugMessage(*instructions)

def raiseDebugMessage(*lines: str):
    """
    Helper function that formats each line as if it were fed to Python's repl.
    Then raises an AssertionError with the formatted message.
    """
    pre = (
        'This check failed. To reproduce its results run the following in the terminal:\n'
        '$ python3\n'
        '>>> from hangman import *\n'
    )

    lines = [l if l.startswith(">>> ") else ">>> " + l for l in lines]
    lines = [l.rstrip("\n") for l in lines]
    
    raise AssertionError(pre + "\n".join(lines))