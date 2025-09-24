import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _basics import *
from checkpy import *

include("klimaat.py")
download("climate.csv", "https://raw.githubusercontent.com/minprog/pyprog/2023/opdrachten/week7/klimaat/climate.csv")

@t.passed(doctest_ok)
@t.test(10)
def has_functions():
    """alle gevraagde functies zijn aanwezig"""
    assert function_defined_in_module("print_basic_info")
    assert function_defined_in_module("extremes")
    assert function_defined_in_module("print_extremes")

@t.passed(doctest_ok)
@t.test(90)
def output_test(test):
    def testMethod():
        o1 = ("""KLIMAATANALYSE

Databestand
-----------
Bestandsnaam: climate.csv
Eerste datum: 01-01-1901
Laatste datum: 31-12-2019

Basisinformatie
---------------
Laagste temperatuur: -11.4° op 26-01-1942
Hoogste temperatuur: 37.5° op 25-07-2019
Gemiddelde temperatuur: 13.6°

Extremen 2010-2019
------------------
In 2010 varieerde de temperatuur tussen -6.1° op 02-12 en 34.4° op 09-07
In 2011 varieerde de temperatuur tussen -0.1° op 31-01 en 32.2° op 28-06
In 2012 varieerde de temperatuur tussen -5.1° op 03-02 en 33.0° op 19-08
In 2013 varieerde de temperatuur tussen -2.8° op 17-01 en 34.0° op 02-08
In 2014 varieerde de temperatuur tussen 1.0° op 03-12 en 32.9° op 19-07
In 2015 varieerde de temperatuur tussen -1.3° op 23-01 en 33.1° op 01-07
In 2016 varieerde de temperatuur tussen -0.8° op 29-12 en 32.9° op 20-07
In 2017 varieerde de temperatuur tussen -1.9° op 18-01 en 31.9° op 27-05
In 2018 varieerde de temperatuur tussen -4.6° op 28-02 en 35.7° op 26-07
In 2019 varieerde de temperatuur tussen -1.1° op 24-01 en 37.5° op 25-07""")

        o15 = ("""CLIMATE ANALYSIS

Data file
-----------
Filename: climate.csv
First date: 01-01-1901
Last date: 31-12-2019

Basic information
-----------------
Lowest temperature: -11.4° on 26-01-1942
Highest temperature: 37.5° on 25-07-2019
Average temperature: 13.6°

Extremes 2010-2019
------------------
In 2010 the temperature varied between -6.1° on 02-12 and 34.4° on 09-07
In 2011 the temperature varied between -0.1° on 31-01 and 32.2° on 28-06
In 2012 the temperature varied between -5.1° on 03-02 and 33.0° on 19-08
In 2013 the temperature varied between -2.8° on 17-01 and 34.0° on 02-08
In 2014 the temperature varied between 1.0° on 03-12 and 32.9° on 19-07
In 2015 the temperature varied between -1.3° on 23-01 and 33.1° on 01-07
In 2016 the temperature varied between -0.8° on 29-12 and 32.9° on 20-07
In 2017 the temperature varied between -1.9° on 18-01 and 31.9° on 27-05
In 2018 the temperature varied between -4.6° on 28-02 and 35.7° on 26-07
In 2019 the temperature varied between -1.1° on 24-01 and 37.5° on 25-07""")

        o2 = ("""CLIMATE ANALYSIS

Data file
-----------
Filename: climate.csv
First date: 01-01-1901
Last date: 31-12-2019

Basic information
-----------------
Lowest temperature: -11.4° on 26-01-1942
Highest temperature: 37.5° on 25-07-2019
Average temperature: 13.6°

Extremes 2010-2019
------------------
In 2010 the temperature varied between -6.1° on 02-12 and 34.4° on 09-07
In 2011 the temperature varied between -0.1° on 31-01 and 32.2° on 28-06
In 2012 the temperature varied between -5.1° on 03-02 and 33.0° on 19-08
In 2013 the temperature varied between -2.8° on 17-01 and 34.0° on 02-08
In 2014 the temperature varied between 1.0° on 3-12 and 32.9° on 19-07
In 2015 the temperature varied between -1.3° on 23-01 and 33.1° on 01-07
In 2016 the temperature varied between -0.8° on 29-12 and 32.9° on 20-07
In 2017 the temperature varied between -1.9° on 18-01 and 31.9° on 27-05
In 2018 the temperature varied between -4.6° on 28-02 and 35.7° on 26-07
In 2019 the temperature varied between -1.1° on 24-01 and 37.5° on 25-07""")
        output = lib.outputOf(test.fileName, overwriteAttributes = [("__name__", "__main__")]).strip()
        output = "\n".join(output.split("\n")[:26])
        print(output)
        return output == o1.strip() or output == o2.strip() or output == o15.strip()
    test.test = testMethod
    test.description = lambda : "print exact de juiste uitvoer t/m extremen (eerste 26 regels)"

@t.passed(doctest_ok)
@t.test(90)
def test_hittegolven(test):
    """functie `heatwaves` werkt correct"""
    assert getFunction("heatwaves")('climate.csv', 1901, 1920) == {1911: ((8, 8), (14, 8))}, "geprobeerd: heatwaves('climate.csv', 1901, 1920)"
    bla = getFunction("heatwaves")('climate.csv', 1901, 2019)
    assert 1959 not in bla.keys(), "let op: 1959 heeft geen hittegolf, want een hittegolf is minstens 5 dagen lang"
    assert getFunction("heatwaves")('climate.csv', 1901, 2019) == {1911: ((8, 8), (14, 8)), 1922: ((21, 5), (25, 5)), 1923: ((5, 7), (14, 7)), 1941: ((20, 6), (26, 6)), 1947: ((14, 8), (21, 8)), 1948: ((26, 7), (30, 7)), 1975: ((29, 7), (15, 8)), 1976: ((23, 6), (9, 7)), 1982: ((29, 7), (4, 8)), 1983: ((4, 7), (12, 7)), 1990: ((26, 7), (4, 8)), 1994: ((19, 7), (31, 7)), 1995: ((29, 7), (3, 8)), 1997: ((5, 8), (13, 8)), 1999: ((28, 7), (4, 8)), 2001: ((22, 8), (26, 8)), 2003: ((31, 7), (13, 8)), 2004: ((2, 8), (11, 8)), 2005: ((18, 6), (24, 6)), 2006: ((30, 6), (6, 7)), 2013: ((21, 7), (27, 7)), 2015: ((30, 6), (5, 7)), 2018: ((15, 7), (27, 7)), 2019: ((22, 7), (27, 7))}, "geprobeerd: heatwaves('climate.csv', 1901, 2019)"
