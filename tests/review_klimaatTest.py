import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

from checkpy import *

include("review_klimaat.py")
download("climate.csv", "https://raw.githubusercontent.com/minprog/pyprog/2022/opdrachten/week5/klimaat/climate.csv")

@t.test(1)
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
        return output == o1.strip() or output == o2.strip() or output == o15.strip()
    test.test = testMethod
    test.description = lambda : "prints exactly the right output"
