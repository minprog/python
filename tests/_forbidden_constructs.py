"""
Reusable checkpy module for forbidden constructs, with grouped rules.

Usage:
    import forbidden_construct_checker as fcc

    # Only groups:
    fcc.disallow(groups=["functional", "strings_advanced"])

    # Only specific rules:
    fcc.disallow(rules=["eval", "tabs"])

    # Groups + rules:
    fcc.disallow(groups=["typing_old"], rules=["eval"])

    # Clear selection (no rules active):
    fcc.disallow()

    check_forbidden_constructs = fcc.check_forbidden_constructs
"""

from typing import Callable, Iterable

import checkpy.tests as t
from _static_analysis import (
    has_string, has_call, has_import, has_syntax_error,
    has_generators, not_has_stringmethods, not_has_stringmult
)

# --- single source of truth: groups -> rules ---
RULE_GROUPS: dict[str, dict[str, tuple[Callable[[], bool], str]]] = {
    "basic_formatting": {
        "tabs": (lambda: has_string("\t"), "let op dat je geen tabs gebruikt"),
    },
    "deprecations": {
        "Optional": (lambda: has_string("Optional"), "gebruik ... | None i.p.v. Optional[...]"),
        "List": (lambda: has_string("List["), "gebruik list[...] i.p.v. List[...]"),
        "Tuple": (lambda: has_string("Tuple["), "gebruik tuple[...] i.p.v. Tuple[...]"),
        "Dict": (lambda: has_string("Dict["), "gebruik dict[...] i.p.v. Dict[...]"),
        "Set": (lambda: has_string("Set["), "gebruik set[...] i.p.v. Set[...]"),
    },
    "string_builtins": {
        "stringmult": (lambda: not_has_stringmethods(), "gebruik geen string * getal"),
        "stringmethods": (lambda: not_has_stringmult(), "gebruik geen string-methods"),
    },
    "list_builtins": {
        "min_max": (lambda: has_call("min", "max"), "gebruik geen min() of max()"),
        "sorted": (lambda: has_call("sorted"), "gebruik geen sorted()"),
    },
    "functional_style": {
        "map": (lambda: has_call("map"), "gebruik geen map()"),
        "zip": (lambda: has_call("zip"), "gebruik geen zip()"),
        "generators": (lambda: has_generators(), "let op dat je geen [... for ...] gebruikt"),
        "all_any": (lambda: has_call("all", "any"), "gebruik geen all() of any()"),
        "eval": (lambda: has_call("eval"), "gebruik geen eval()"),
    },
    "stdlib_restrictions": {
        "import_math": (lambda: has_import("math"), "gebruik geen import math"),
    },
}

# Derived flat index for validation/lookup
ALL_RULES: dict[str, tuple[Callable[[], bool], str]] = {
    rule: check
    for group in RULE_GROUPS.values()
    for rule, check in group.items()
}

# Active rules (set by disallow())
ACTIVE_RULES: dict[str, tuple[Callable[[], bool], str]] | None = None


def disallow(*, groups: Iterable[str] = (), rules: Iterable[str] = ()) -> None:
    """
    Enable rules from the given groups and/or explicit rule keys.
    Both args default to empty = select nothing.

    Examples:
        disallow(groups=["functional", "strings_advanced"])
        disallow(rules=["eval", "tabs"])
        disallow(groups=["typing_old"], rules=["eval"])
        disallow()  # selects nothing
    """
    global ACTIVE_RULES

    selected: set[str] = set()

    # Validate groups and collect their rules
    groups = list(groups)
    unknown_groups = [g for g in groups if g not in RULE_GROUPS]
    if unknown_groups:
        raise ValueError(f"Unknown group(s): {unknown_groups}")

    for g in groups:
        selected.update(RULE_GROUPS[g].keys())

    # Validate explicit rule keys and add them
    rules = list(rules)
    unknown_rules = [r for r in rules if r not in ALL_RULES]
    if unknown_rules:
        raise ValueError(f"Unknown rule(s): {unknown_rules}")

    selected.update(rules)

    ACTIVE_RULES = {k: ALL_RULES[k] for k in sorted(selected)}


def disallow_all() -> None:
    """Enable all rules."""
    global ACTIVE_RULES
    ACTIVE_RULES = dict(ALL_RULES)


@t.test()
def check_forbidden_constructs(test):
    """check op verboden constructies"""
    def testMethod():
        if ACTIVE_RULES is None:
            raise RuntimeError(
                "forbidden_construct_checker.disallow(...) moet worden "
                "aangeroepen voordat check_forbidden_constructs kan draaien"
            )

        if (lineno := has_syntax_error()):
            return False, f"de code bevat een syntax error op regel {lineno}"

        for key, (check_fn, message) in ACTIVE_RULES.items():
            if check_fn():
                return False, message

        return True

    test.test = testMethod


# Expose as methods on the test function
check_forbidden_constructs.disallow = disallow
check_forbidden_constructs.disallow_all = disallow_all
