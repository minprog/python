from checkpy import *
from _basics import *
from _static_analysis import *

import ast

@t.passed(doctest_ok)
def test_point(test):
    """classes `Point` en `LineSegment` werken correct"""
    point1 = getModule().Point(1, 1)
    point2 = getModule().Point(3, 2)
    line_segment = getModule().LineSegment(point1, point2)
    assert line_segment.slope() == 0.5
    assert line_segment.length() == 2.23606797749979
