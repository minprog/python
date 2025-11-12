from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def test_point():
    """class `Point` werkt correct"""
    Point = getModule().Point

    p1 = Point(2, 3)
    p2 = Point(5, -1)

    # attributen
    assert p1.x == 2
    assert p1.y == 3
    assert p2.x == 5
    assert p2.y == -1

    # __str__
    s = str(p1)
    assert s == "(2, 3)"

    # __add__
    p3 = p1 + p2
    # TODO avoid this horrible _function bc Point is wrapped by CheckPy
    assert isinstance(p3, Point._function)
    assert (p3.x, p3.y) == (7, 2)
    assert str(p3) == "(7, 2)"

    # distance_to
    d = p1.distance_to(p2)
    assert abs(d - ((5 - 2)**2 + (-1 - 3)**2)**0.5) < 1e-9
