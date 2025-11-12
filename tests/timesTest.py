from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest_all
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest_all)
def test_time():
    """class `Time` werkt correct"""
    Time = getModule().Time

    t = Time("10:31:00")

    # attributen
    assert hasattr(t, "hours")
    assert hasattr(t, "minutes")
    assert hasattr(t, "seconds")

    # __str__
    assert str(t) == "10:31:00"

    # + seconden
    t2 = t + 90
    assert isinstance(t2, Time._function)
    assert str(t2) == "10:32:30"

    # - seconden
    t3 = t - 45
    assert isinstance(t3, Time._function)
    assert str(t3) == "10:30:15"

    # next_hour
    nh = t.next_hour()
    assert isinstance(nh, Time._function)
    assert str(nh) == "11:31:00"

    # prev_minute
    pm = t.prev_minute()
    assert isinstance(pm, Time._function)
    assert str(pm) == "10:30:00"

    # originele tijd onveranderd
    assert str(t) == "10:31:00"

    # overgang naar vorige dag
    t4 = Time("00:00:30") - 45
    assert str(t4) == "23:59:45"

    # overgang naar volgende dag
    t5 = Time("23:59:30") + 90
    assert str(t5) == "00:01:00"
