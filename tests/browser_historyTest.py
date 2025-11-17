from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, mypy_strict, doctest
# forbidden_constructs.disallow_all()

@passed(checkstyle, mypy_strict, doctest)
def test_class():
    """class `BrowserHistory` is aanwezig"""
    BrowserHistory = getModule().BrowserHistory
    assert BrowserHistory()

@passed(test_class)
def test_visit():
    """class werkt correct voor 1x visit"""
    BrowserHistory = getModule().BrowserHistory
    bh = BrowserHistory()
    bh.visit("a.com")
    assert bh.current() == "a.com"

@passed(test_class)
def test_back():
    """class werkt met 2x visit en 1x back"""
    BrowserHistory = getModule().BrowserHistory
    bh = BrowserHistory()
    bh.visit("a")
    bh.visit("b")
    bh.back()
    assert bh.current() == "a"

@passed(test_class)
def test_visit_cuts_forward():
    """class knipt de toekomst weg als je back gaat en dan een visit doet"""
    BrowserHistory = getModule().BrowserHistory
    bh = BrowserHistory()
    bh.visit("a.com")
    bh.visit("a")
    bh.visit("b")
    bh.back()
    bh.visit("c")
    assert bh.current() == "c"
    # forward must be gone
    assert bh.find("b") == []

@passed(test_class)
def test_back_at_start():
    """na 1x visit en 1x back zijn we nog steeds bij de start"""
    BrowserHistory = getModule().BrowserHistory
    bh = BrowserHistory()
    bh.visit("a")
    bh.back()
    assert bh.current() == "a"

@passed(test_class)
def test_forward():
    """na 2x visit, 1x back en 1x forward zijn we nog steeds bij het einde"""
    BrowserHistory = getModule().BrowserHistory
    bh = BrowserHistory()
    bh.visit("a")
    bh.visit("b")
    bh.back()
    bh.forward()
    assert bh.current() == "b"

@passed(test_class)
def test_find_case_insensitive():
    """methode `find` werkt case insensitive"""
    BrowserHistory = getModule().BrowserHistory
    bh = BrowserHistory()
    bh.visit("Example.com")
    bh.visit("test.com")
    assert bh.find("exa") == ["Example.com"]

@passed(test_class)
def test_clear():
    """methode `clear` werkt en `current` geeft daarna None of een exception"""
    BrowserHistory = getModule().BrowserHistory
    bh = BrowserHistory()
    bh.visit("a")
    bh.visit("b")
    bh.clear()
    # history empty, current should raise
    try:
        x = bh.current()
    except:
        return
    if x != None:
        raise AssertionError("geen exception gekregen en return was ook niet None")
