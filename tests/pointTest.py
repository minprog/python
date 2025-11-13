from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def test_point():
    """class `Point` werkt correct"""
    Point = getModule().Point

    p1 = Point(2, 3)
    p2 = Point(5, -1)

    # attributen
    assert p1.x == 2, "de x van Point(2, 3) zou 2 moeten zijn"
    assert p1.y == 3, "de y van Point(2, 3) zou 3 moeten zijn"
    assert p2.x == 5, "de x van Point(5, -1) zou 5 moeten zijn"
    assert p2.y == -1, "de y van Point(5, -1) zou -1 moeten zijn"

    # __str__
    s = str(p1)
    assert s == "(2, 3)", "als we Point(2, 3) printen moet er (2, 3) uitkomen"

    # __add__
    p3 = p1 + p2
    # TODO avoid this horrible _function bc Point is wrapped by CheckPy
    assert isinstance(p3, Point._function), "als we twee Points optellen moet er ook weer een Point uitkomen"
    assert (p3.x, p3.y) == (7, 2), "als we (2, 3) en (5, -1) optellen moet er (7, 2) uitkomen"
    assert str(p3) == "(7, 2)", "als we Point(7, 2) printen, als resultaat van een optelling, moet er (7, 2) uitkomen"

    # distance_to
    d = p1.distance_to(p2)
    assert abs(d - ((5 - 2)**2 + (-1 - 3)**2)**0.5) < 1e-9, f"de afstand van (2, 3) naar (5, -1) moet 5.0 zijn"
