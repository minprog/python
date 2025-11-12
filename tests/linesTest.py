from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def test_point():
    """classes `Point` en `LineSegment` werken correct"""
    point1 = getModule().Point(1, 1)
    point2 = getModule().Point(3, 2)
    line_segment = getModule().LineSegment(point1, point2)
    if line_segment.slope() != 0.5:
        raise AssertionError("expected line segment from (1, 1) to (3, 2) to have slope 0.5")
    if line_segment.length() != 2.23606797749979:
        raise AssertionError("expected line segment from (1, 1) to (3, 2) to have length 2.23606797749979")
