from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def test_point():
    """class `RGB` werkt correct"""
    RGB = getModule().RGB
    c = RGB(100, 150, 200)

    # init
    assert c.red == 100, "red van RGB(100, 150, 200) moet 100 zijn"
    assert c.green == 150, "green van RGB(100, 150, 200) moet 150 zijn"
    assert c.blue == 200, "blue van RGB(100, 150, 200) moet 200 zijn"

    # to_hex
    assert isinstance(c.to_hex(), str), "to_hex() moet een str opleveren"
    assert c.to_hex().lower() == "#6496c8", "to_hex() van RGB(100, 150, 200) moet #6496c8 zijn"

    # invert
    inv = c.invert()
    assert inv.red == 155, "red van de invert van RGB(100, 150, 200) moet 155 zijn"
    assert inv.green == 105, "green van de invert van RGB(100, 150, 200) moet 105 zijn"
    assert inv.blue == 55, "blue van de invert van RGB(100, 150, 200) moet 55 zijn"

    # lighter(0.2)
    lighter = c.lighter(0.2)
    assert lighter.red == round(100 + 0.2 * (255 - 100)), f"red van de lighter(0.2) van RGB(100, 150, 200) moet {round(100 + 0.2 * (255 - 100))} zijn"
    assert lighter.green == round(150 + 0.2 * (255 - 150)), f"green van de lighter(0.2) van RGB(100, 150, 200) moet {round(150 + 0.2 * (255 - 150))} zijn"
    assert lighter.blue == round(200 + 0.2 * (255 - 200)), f"blue van de lighter(0.2) van RGB(100, 150, 200) moet {round(200 + 0.2 * (255 - 200))} zijn"

    # darker(0.3)
    darker = c.darker(0.3)
    assert darker.red == round(100 * (1 - 0.3)), f"red van de darker(0.3) van RGB(100, 150, 200) moet {round(100 * (1 - 0.3))} zijn"
    assert darker.green == round(150 * (1 - 0.3)), f"green van de darker(0.3) van RGB(100, 150, 200) moet {round(150 * (1 - 0.3))} zijn"
    assert darker.blue == round(200 * (1 - 0.3)), f"blue van de darker(0.3) van RGB(100, 150, 200) moet {round(100 + 0.2 * (255 - 100))} zijn"

    # originele kleur blijft gelijk
    assert (c.red, c.green, c.blue) == (100, 150, 200), "na het aanroepen van methods op een kleur moet deze originele kleur onveranderd zijn"
