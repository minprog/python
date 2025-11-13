from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, forbidden_constructs, mypy_strict, doctest
forbidden_constructs.disallow_all()

@passed(checkstyle, forbidden_constructs, mypy_strict, doctest)
def test_time():
    """class `Time` werkt correct"""
    Time = getModule().Time

    t = Time("10:31:00")

    # attributen
    assert hasattr(t, "hours"), "een aangemaakt Time-object moet altijd een attribuut hours hebben"
    assert hasattr(t, "minutes"), "een aangemaakt Time-object moet altijd een attribuut minutes hebben"
    assert hasattr(t, "seconds"), "een aangemaakt Time-object moet altijd een attribuut seconds hebben"

    # __str__
    assert str(t) == "10:31:00", "de str van Time('10:31:00') moet ook '10:31:00' zijn"

    # + seconden
    t2 = t + 90
    # NOTE: Time._function is actually the student-provided Time class (not a function of it)
    assert isinstance(t2, Time._function), "als je Time + iets doet moet er een Time uitkomen"
    assert str(t2) == "10:32:30", "Time('10:31:00') + 90 moet 10:32:30 zijn"

    # - seconden
    t3 = t - 45
    assert isinstance(t3, Time._function)
    assert str(t3) == "10:30:15", "Time('10:31:00') - 45 moet 10:30:15 zijn"

    # next_hour
    nh = t.next_hour()
    assert isinstance(nh, Time._function)
    assert str(nh) == "11:00:00", "de 'next hour' van Time('10:31:00') moet 11:00:00 zijn"

    # prev_minute
    pm = t.prev_minute()
    assert isinstance(pm, Time._function)
    assert str(pm) == "10:30:00", "de 'prev minute' van Time('10:31:00') moet 10:30:00 zijn"

    # originele tijd onveranderd
    assert str(t) == "10:31:00", "na optellen en aftrekken bij een Time moet deze onveranderd zijn"

    # overgang naar vorige dag
    t4 = Time("00:00:30") - 45
    assert str(t4) == "23:59:45", "Time('00:00:30') - 45 moet 23:59:45 zijn"

    # overgang naar volgende dag
    t5 = Time("23:59:30") + 90
    assert str(t5) == "00:01:00", "Time('23:59:30') + 90 moet 00:01:00 zijn"
