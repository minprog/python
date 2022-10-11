import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *

@t.test(1)
def generate_virus_length(test):
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)

        if not isinstance(generate_virus(1), str):
            return False, "expected generateVirus() to return a str"

        for i in range(10):
            if not len(generate_virus(i)) == i:
                return False, f"expected generate_virus({i}) to produce a virus of length {i}"

        return True

    test.test = testMethod
    test.description = lambda : "generate_virus() produces viruses of the specified length"

@t.test(1)
def generate_virus_elements(test):
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)

        pairs = "".join([generate_virus(10) for _ in range(100)])

        if any([el not in "AGTC" for el in pairs]):
            return False

        return True

    test.test = testMethod
    test.description = lambda : "generate_virus() produces viruses consisting only of A, T, G and C"

@t.test(1)
def mutate_length(test):
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        mutate = lib.getFunction("mutate", test.fileName)

        if not isinstance(mutate("AAAA"), str):
            return False, "expected mutate() to return a str"

        try:
            for i in range(1, 10):
                v = generate_virus(i)
                if not len(v) == len(mutate(v)):
                    return False, f"expected mutate() to produce a virus of the same length as the parent"
        except ValueError:
            return False, "it seems that mutate gives an error, are you sure it works for viruses of length 1?"

        return True

    test.test = testMethod
    test.description = lambda : "mutate() produces viruses of the same length as the parent"

@t.test(1)
def mutate_elements(test):
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        mutate = lib.getFunction("mutate", test.fileName)

        pairs = "".join([mutate(generate_virus(10)) for _ in range(100)])

        if any([el not in "AGTC" for el in pairs]):
            return False, "expected mutate() to return only combinations of AGTC"

        return True

    test.test = testMethod
    test.description = lambda : "mutate() produces viruses consisting only of A, T, G and C"

@t.test(1)
def mutate_one_difference(test):
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        mutate = lib.getFunction("mutate", test.fileName)

        off_by_one = lambda col1, col2 : sum(a != b for a, b in zip(col1, col2)) == 1

        for v in [generate_virus(i) for i in range(1, 100)]:
            mutated_v = mutate(v)
            if not off_by_one(mutated_v, v):
                return False, f"expected mutate({v}) to return a virus with only one mutation, not {mutated_v}"

        return True

    test.test = testMethod
    test.description = lambda : "mutate() produces viruses that differ exactly one element from the parent"

@t.test(1)
def kill_no_modify(test):
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        kill = lib.getFunction("kill", test.fileName)

        if not isinstance(kill(["AAAA"], 0.25), list):
            return False, "expected kill() to return a list"

        viruses = [generate_virus(4) for i in range(10)]
        viruses_copy = viruses[:]
        new_viruses = kill(viruses, 1)

        if viruses != viruses_copy:
            return False, f"the viruses passed in changed from {viruses_copy} to {viruses}"

        return True

    test.test = testMethod
    test.description = lambda : "kill() does not modify the list of viruses it accepts as argument"

@t.test(1)
def kill_no_new(test):
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        kill = lib.getFunction("kill", test.fileName)

        viruses = [generate_virus(4) for i in range(100)]
        new_viruses = kill(viruses, 0.25)

        if set(new_viruses).difference(set(viruses)) or len(new_viruses) > len(viruses):
            return False, "expected no new viruses"

        return True

    test.test = testMethod
    test.description = lambda : "kill() does not produce any new viruses"

@t.test(1)
def kill_enough(test):
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        kill = lib.getFunction("kill", test.fileName)

        viruses = [generate_virus(4) for i in range(100)]
        avg_pop_size = sum(len(kill(viruses[:], 0.25)) for i in range(1000)) / 1000

        if not 70 <= avg_pop_size <= 80:
            raise check50.Failure(f"expected roughly 25% of the population to die with mortality_prob of 0.25, but {100 - avg_pop_size}% died!")

        return True

    test.test = testMethod
    test.description = lambda : "kill() kills enough viruses according to mortality probability"

@t.test(1)
def reproduce_parents(test):
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        reproduce = lib.getFunction("reproduce", test.fileName)

        viruses = [generate_virus(4) for i in range(100)]
        new_viruses = reproduce(viruses, 0.25, 0)

        if not isinstance(new_viruses, list):
            return False, "expected reproduce() to return a list"

        if not new_viruses == viruses:
            if len(new_viruses) < len(viruses):
                return False, "did not expect fewer viruses after reproduce()"
            elif len(new_viruses) > len(viruses):
                return False, "expected no new viruses"
            else:
                return False, "did not expect to find different viruses"

        return True

    test.test = testMethod
    test.description = lambda : "reproduce() with reproduction_rate=0 produces no new viruses"

@t.test(1)
def reproduce_avg(test):
    def testMethod():
        generate_virus = lib.getFunction("generate_virus", test.fileName)
        reproduce = lib.getFunction("reproduce", test.fileName)

        viruses = [generate_virus(4) for i in range(100)]
        new_viruses = reproduce(viruses, 0.25, 0)

        n_trials = 1000
        avg_pop_size = sum(len(reproduce(viruses[:], 0.25, 0.50)) for _ in range(n_trials)) / n_trials

        if not 145 <= avg_pop_size <= 155:
            return False, f"expected roughly a 50% increase in population with a reproductionRate of .5, not {avg_pop_size - 100}%"

        return True

    test.test = testMethod
    test.description = lambda : "reproduce() produces enough viruses on avg according to reproduction_rate"

@t.test(1)
def is_resistent_AAA(test):
    def testMethod():
        if not asserts.fileContainsFunctionDefinitions(test.fileName, 'is_resistant'):
            return False, "is_resistant() is not defined (check the spelling!)"

        is_resistant = lib.getFunction("is_resistant", test.fileName)

        if is_resistant("AAA") != True:
            return False, "expected AAA to be resistant"
        if is_resistant("AAGGAA") != False:
            return False, "expected AAGGAA to not be resistant"
        if is_resistant("ATGCAATGCAATGGGCCCCTTTAAACCCT") != True:
            return False, "expected ATGCAATGCAATGGGCCCCTTTAAACCCT to be resistant"

        return True

    test.test = testMethod
    test.description = lambda : "is_resistant() works correctly"

@t.test(1)
def simulate_medicine_length(test):
    def testMethod():
        simulate = lib.getFunction("simulate", test.fileName)

        viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
        sim_results = simulate(viruses, 0, 0, 0, 100, 500)

        if not isinstance(sim_results, list):
            return False, "expected simulate() to return a list"

        if not len(sim_results) == 501:
            return False, f"expected a list of 501 long with timesteps=500, but found a list {len(sim_results)} long"

        return True

    test.test = testMethod
    test.description = lambda : "simulate() produces a list of the correct length"

@t.test(1)
def simulate_medicine_fluctuations(test):
    def testMethod():
        simulate = lib.getFunction("simulate", test.fileName)

        viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20

        for pop_size in simulate(viruses, 0, 0, 0, 100, 500):
            if pop_size != 100:
                return False, f"expected 100 viruses, but found {pop_size}"

        return True

    test.test = testMethod
    test.description = lambda : "simulate(viruses, 0, 0, 0, 100) shows no fluctuations in population size"

@t.test(1)
def simulate_medicine_avg(test):
    def testMethod():
        simulate = lib.getFunction("simulate", test.fileName)

        viruses = ["GGGG", "AAAA", "TTTT", "GGGG", "ATGC"] * 20
        n_trials = 100
        timesteps = 1000

        avg = lambda : sum(simulate(viruses[:], 0.1, 0.1, 0.5, 100, timesteps)) / timesteps
        avg_pop_size = sum(avg() for _ in range(n_trials)) / n_trials

        if not 50 <= avg_pop_size <= 75:
            return False, f"expected an average population size of roughly 50 to 65, but found {avg_pop_size}"

        return True

    test.test = testMethod
    test.description = lambda : "simulate(viruses, 0.1, 0.1, 0.5, 100) yields reasonable results"
    test.timeout = lambda: 120
