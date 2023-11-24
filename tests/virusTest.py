import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

# main kan hier gezeur geven
from _remove_main import *

from checkpy import monkeypatch
monkeypatch.patchMatplotlib()

# basic checks met custom regellengtes
import os
os.environ['MAX_LINE_LENGTH'] = '115'
os.environ['MAX_DOC_LENGTH'] = '110'
from _basics import *

@t.passed(doctest_ok)
@t.test(10)
def generate_virus_length(test):
    """generate_virus() maakt virussen van de opgegeven lengte"""
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)

        if not isinstance(generate_virus(1), str):
            return False, "generateVirus() zou een string moeten returnen"

        for i in range(10):
            if not len(generate_virus(i)) == i:
                return False, f"generate_virus({i}) zou een virus van lengte {i} moeten geven"

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(20)
def generate_virus_elements(test):
    """generate_virus() maakt virussen die alleen bestaan uit A, T, G en C"""
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)

        pairs = "".join([generate_virus(10) for _ in range(100)])

        if any([el not in "AGTC" for el in pairs]):
            return False

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(30)
def mutate_length(test):
    """mutate() maakt virus met dezelfde lengte als het origineel"""
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        mutate = lib.getFunction("mutate", test.fileName)

        if not isinstance(mutate("AAAA"), str):
            return False, "mutate() zou een string moeten returnen"

        try:
            for i in range(1, 10):
                v = generate_virus(i)
                if not len(v) == len(mutate(v)):
                    return False, f"mutate({v}) gaf {mutate(v)}"
        except:
            return False, "mutate geeft een fout; werkt de functie ook voor een virus van lengte 1?"

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(40)
def mutate_elements(test):
    """mutate() maakt virussen die alleen bestaan uit A, T, G en C"""
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        mutate = lib.getFunction("mutate", test.fileName)

        pairs = "".join([mutate(generate_virus(10)) for _ in range(100)])

        if any([el not in "AGTC" for el in pairs]):
            return False, "expected mutate() to return only combinations of AGTC"

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(50)
def mutate_one_difference(test):
    """mutate() maakt virussen die precies één verschillen van het origineel"""
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        mutate = lib.getFunction("mutate", test.fileName)

        off_by_one = lambda col1, col2 : sum(a != b for a, b in zip(col1, col2)) == 1

        try:
            for v in [generate_virus(i) for i in range(1, 100)]:
                mutated_v = mutate(v)
                if not off_by_one(mutated_v, v):
                    return False, f"mutate({v}) gaf {mutated_v}"
        except:
            return False, "mutate geeft een fout; werkt de functie ook voor een virus van lengte 1?"

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(60)
def kill_no_modify(test):
    """kill() met een kans van 0 verandert niets aan de lijst virussen die opgegeven wordt"""
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        kill = lib.getFunction("kill", test.fileName)

        if not isinstance(kill(["AAAA"], 0.25), list):
            return False, "kill() zou een lijst moeten returnen"

        viruses = [generate_virus(4) for i in range(10)]
        viruses_copy = viruses[:]
        new_viruses = kill(viruses, 0)

        if new_viruses != viruses_copy:
            return False, f"{viruses_copy} werd ten onrechte aangepast naar {new_viruses}"

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(70)
def kill_no_new(test):
    """kill() voegt geen virussen toe aan de opgegeven lijst"""
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        kill = lib.getFunction("kill", test.fileName)

        viruses = [generate_virus(4) for i in range(100)]
        new_viruses = kill(viruses, 0.25)

        if set(new_viruses).difference(set(viruses)) or len(new_viruses) > len(viruses):
            return False

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(80)
def kill_enough(test):
    """kill() verwijdert ongeveer de opgegeven hoeveelheid virussen uit de opgegeven lijst"""
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        kill = lib.getFunction("kill", test.fileName)

        viruses = [generate_virus(4) for i in range(100)]
        avg_pop_size = sum(len(kill(viruses[:], 0.25)) for i in range(1000)) / 1000

        if not 70 <= avg_pop_size <= 80:
            raise check50.Failure(f"met een mortality_prob van 0.25 zou ongeveer 25% moeten uitvallen, maar het is {100 - avg_pop_size}%")

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(90)
def reproduce_parents(test):
    """reproduce() met een reproduction_rate=0 voegt geen nieuwe virussen toe"""
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        reproduce = lib.getFunction("reproduce", test.fileName)

        viruses = [generate_virus(4) for i in range(100)]
        new_viruses = reproduce(viruses, 0.25, 0)

        if not isinstance(new_viruses, list):
            return False, "de functie zou een lijst moeten returnen"

        if not new_viruses == viruses:
            if len(new_viruses) < len(viruses):
                return False, "de functie zou geen kortere lijst moeten returnen"
            elif len(new_viruses) > len(viruses):
                return False, "de functie zou geen langere lijst moeten returnen"
            else:
                return False, "de functie geeft andere virussen terug dan opgegeven"

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(100)
def reproduce_avg(test):
    """reproduce() met een reproduction_rate=0.5 voegt ongeveer 50% nieuwe virussen toe"""
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        reproduce = lib.getFunction("reproduce", test.fileName)

        viruses = [generate_virus(4) for i in range(100)]
        new_viruses = reproduce(viruses, 0.25, 0)

        n_trials = 1000
        avg_pop_size = sum(len(reproduce(viruses[:], 0.25, 0.50)) for _ in range(n_trials)) / n_trials

        if not 145 <= avg_pop_size <= 155:
            return False, f"gemeten groei is ongeveer {avg_pop_size - 100}%"

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(110)
def is_resistant_AAA(test):
    """is_resistant() werkt correct"""
    def testMethod():
        if not asserts.fileContainsFunctionDefinitions(test.fileName, 'is_resistant'):
            return False, "is_resistant() is niet gedefinieerd (verkeerd gespeld?)"

        is_resistant = lib.getFunction("is_resistant", test.fileName)

        if is_resistant("AAA") != True:
            return False, "AAA zou resistent moeten zijn"
        if is_resistant("AAGGAA") != False:
            return False, "AAGGAA zou niet resistent moeten zijn"
        if is_resistant("ATGCAATGCAATGGGCCCCTTTAAACCCT") != True:
            return False, "ATGCAATGCAATGGGCCCCTTTAAACCCT zou resistent moeten zijn"

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(120)
def simulate_medicine_length(test):
    """simulate() maakt een lijst van de juiste lengte"""
    def testMethod():
        simulate = lib.getFunction("simulate", test.fileName)

        viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
        sim_results = simulate(viruses, 0, 0, 0, 100, 500)

        if not isinstance(sim_results, list):
            return False, "de functie zou een lijst moeten returnen"

        if not len(sim_results) == 501:
            return False, f"bij timesteps=500 moet lengte 501 zijn, maar is {len(sim_results)}"

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(130)
def simulate_medicine_fluctuations(test):
    """simulate(viruses, 0, 0, 0, 100) vertoont geen fluctuaties in populatiegrootte"""
    def testMethod():
        simulate = lib.getFunction("simulate", test.fileName)

        viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20

        for pop_size in simulate(viruses, 0, 0, 0, 100, 500):
            if pop_size != 100:
                return False, f"100 virussen verwacht, maar was {pop_size}"

        return True
    test.test = testMethod

@t.passed(doctest_ok)
@t.test(140)
def simulate_medicine_avg(test):
    """simulate(viruses, 0.1, 0.1, 0.5, 100) geeft te verwachten resultaten"""
    def testMethod():
        simulate = lib.getFunction("simulate", test.fileName)

        viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
        n_trials = 100
        timesteps = 100

        avg = lambda : sum(simulate(viruses[:], 0.1, 0.1, 0.5, 100, timesteps)) / timesteps
        avg_pop_size = sum(avg() for _ in range(n_trials)) / n_trials

        if not 85 <= avg_pop_size <= 90:
            return False, f"gemiddelde van 85 tot 90 verwacht, maar was {avg_pop_size}"

        return True

    test.test = testMethod
    test.timeout = lambda: 120
