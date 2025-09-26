from checkpy import *
from _basics import *
from _pyprog_tools import *

import ast

@passed(doctest_ok)
def test_point():
    """classes `Point` en `LineSegment` werken correct"""
    point1 = getModule().Point(1, 1)
    point2 = getModule().Point(3, 2)
    line_segment = getModule().LineSegment(point1, point2)
    if line_segment.slope() != 0.5:
        raise AssertionError("expected line segment from (1, 1) to (3, 2) to have slope 0.5")
    if line_segment.length() != 2.23606797749979:
        raise AssertionError("expected line segment from (1, 1) to (3, 2) to have length 2.23606797749979")
