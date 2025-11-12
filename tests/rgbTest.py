from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def test_point():
    """class `RGB` werkt correct"""
    RGB = getModule().RGB
    c = RGB(100, 150, 200)

    # init
    assert c.red == 100
    assert c.green == 150
    assert c.blue == 200

    # to_hex
    assert isinstance(c.to_hex(), str)
    assert c.to_hex().lower() == "#6496c8"

    # invert
    inv = c.invert()
    assert inv.red == 155
    assert inv.green == 105
    assert inv.blue == 55

    # lighter(0.2)
    lighter = c.lighter(0.2)
    assert lighter.red == round(100 + 0.2 * (255 - 100))
    assert lighter.green == round(150 + 0.2 * (255 - 150))
    assert lighter.blue == round(200 + 0.2 * (255 - 200))

    # darker(0.3)
    darker = c.darker(0.3)
    assert darker.red == round(100 * (1 - 0.3))
    assert darker.green == round(150 * (1 - 0.3))
    assert darker.blue == round(200 * (1 - 0.3))

    # originele kleur blijft gelijk
    assert (c.red, c.green, c.blue) == (100, 150, 200)
