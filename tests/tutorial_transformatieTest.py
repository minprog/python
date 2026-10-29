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
def test_kopie():
    """functie `kopie` werkt correct"""
    f = defined("kopie")
    assert f("hallo") == "hallo"
    assert f("") == ""

@test()
def test_hoofdletters():
    """functie `hoofdletters` werkt correct"""
    f = defined("hoofdletters")
    assert f("hallo") == "HALLO"
    assert f("Dag 3!") == "DAG 3!"

@test()
def test_spaties_naar_streepjes():
    """functie `spaties_naar_streepjes` werkt correct"""
    f = defined("spaties_naar_streepjes")
    assert f("hallo daar") == "hallo_daar"
    assert f("een twee drie") == "een_twee_drie"

@test()
def test_verberg_klinkers():
    """functie `verberg_klinkers` werkt correct"""
    f = defined("verberg_klinkers")
    assert f("python") == "pyth*n"
    assert f("Amsterdam") == "*mst*rd*m"

@test()
def test_l337sp34k():
    """functie `l337sp34k` werkt correct"""
    f = defined("l337sp34k")
    assert f("leet") == "1337"
    assert f("Hallo Toto!") == "H4110 7070!"

@test()
def test_verberg_cijfers():
    """functie `verberg_cijfers` werkt correct"""
    f = defined("verberg_cijfers")
    assert f("pincode 1234") == "pincode ####"
    assert f("R2D2") == "R#D#"

@test()
def test_blackout():
    """functie `blackout` werkt correct"""
    f = defined("blackout")
    assert f("Geheim!") == "######!"
    assert f("R2D2 is 1 robot.") == "#2#2 ## 1 #####."

@test()
def test_replace_char():
    """functie `replace_char` werkt correct"""
    f = defined("replace_char")
    assert f("banaan", "a", "o") == "bonoon"
    assert f("hallo daar", " ", "_") == "hallo_daar"

@test()
def test_zonder_spaties():
    """functie `zonder_spaties` werkt correct"""
    f = defined("zonder_spaties")
    assert f("hallo daar") == "hallodaar"
    assert f(" a b c ") == "abc"

@test()
def test_verwijder_n():
    """functie `verwijder_n` werkt correct"""
    f = defined("verwijder_n")
    assert f("banaan") == "baaa"
    assert f("nu niet") == "u iet"

@test()
def test_kopie_met_posities():
    """functie `kopie_met_posities` werkt correct"""
    f = defined("kopie_met_posities")
    assert f("hallo") == "hallo"
    assert f("") == ""

@test()
def test_laatste_letters():
    """functie `laatste_letters` werkt correct"""
    f = defined("laatste_letters")
    assert f("hallo daar") == "or"
    assert f("een twee drie") == "nee"

@test()
def test_verwijder_n_eind():
    """functie `verwijder_n_eind` werkt correct"""
    f = defined("verwijder_n_eind")
    assert f("lopen en fietsen") == "lope e fietse"
    assert f("banaan, nu even.") == "banaa, nu eve."

@test()
def test_eerste_letters():
    """functie `eerste_letters` werkt correct"""
    f = defined("eerste_letters")
    assert f("hallo daar") == "hd"
    assert f("een twee drie") == "etd"

@test()
def test_verwijder_n_begin():
    """functie `verwijder_n_begin` werkt correct"""
    f = defined("verwijder_n_begin")
    assert f("nu niet") == "u iet"
    assert f("banaan,nee") == "banaan,ee"

@test()
def test_stretch():
    """functie `stretch` werkt correct"""
    f = defined("stretch")
    assert f("abc") == "abbccc"
    assert f("Hoi!") == "Hooiii!!!!"
    assert f("") == ""

@test()
def test_autocorrect():
    """functie `autocorrect` werkt correct"""
    f = defined("autocorrect")
    assert f("---") == "-"
    assert f("Dit hier,, dit kan niet de bedoeling   zijn.") == "Dit hier, dit kan niet de bedoeling zijn."
    assert f("") == ""

@test()
def test_spongebob1():
    """functie `spongebob1` werkt correct"""
    f = defined("spongebob1")
    assert f("hello world!") == "hElLo wOrLd!"

@test()
def test_spongebob2():
    """functie `spongebob2` werkt correct"""
    f = defined("spongebob2")
    assert f("hello world!") == "hElLo WoRlD!"

@test(100)
def doctests(test):
    """elke functie heeft voldoende doctests en ze geven allemaal akkoord"""
    def testMethod():
        return check_doctests(test, True)
    test.test = testMethod
    test.fail = lambda info: info
    test.timeout = lambda: 120
