from checkpy import *
from typing import Any
import ast

from checkpy import static

def defines_function(name: str) -> bool:
    check = name in static.getFunctionDefinitions()
    if not check:
        raise AssertionError(f"`{name}` is niet aanwezig")
    return check

def not_defines_function(name: str) -> bool:
    check = name not in static.getFunctionDefinitions()
    if not check:
        raise AssertionError(f"`{name}` is onverwacht aanwezig")
    return check

def not_in_code(construct: type):
    check = construct not in static.AbstractSyntaxTree()
    name = str(construct).split(".")[1].split("'")[0].lower()
    if not check:
        if name in ['list', 'set', 'tuple', 'dict']:
            raise AssertionError(f"{name}s mogen niet gebruikt worden in deze opdracht")
        else:
            raise AssertionError(f"`{name}` mag niet gebruikt worden in deze opdracht")
    return check

def in_code(construct: type):
    check = construct in static.AbstractSyntaxTree()
    name = str(construct).split(".")[1].split("'")[0].lower()
    if not check:
        raise AssertionError(f"`{name}` moet gebruikt worden in deze opdracht")
    return check

def not_has_stringmethods() -> bool:
    tree = ast.parse(static.getSource())
    for n in ast.walk(tree):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            if n.func.attr in ['replace', 'find', 'index']:
                raise AssertionError(f"string-methods zoals {n.func.attr}() mogen niet gebruikt worden")
    return True

def not_has_stringmult() -> bool:
    tree = ast.parse(static.getSource())
    for n in ast.walk(tree):
        if isinstance(n, ast.BinOp) and isinstance(n.op, ast.Mult):
            if (isinstance(n.left, ast.Constant) and isinstance(n.left.value, str)
                or isinstance(n.right, ast.Constant) and isinstance(n.right.value, str)):
                raise AssertionError(f"`*` mag alleen gebruikt worden om getallen te vermenigvuldigen met elkaar")
    return True

def has_syntax_error():
    try:
        compile(static.getSource(), "<your program>", "exec")
    except SyntaxError as error:
        return error.lineno
    return False

def has_string(*forbidden_strings):
    source = static.getSource()
    return any(f in source for f in forbidden_strings)

def has_call(*banned_calls) -> bool:
    found = False

    class Visitor(ast.NodeVisitor):
        def visit_Name(self, node: ast.Name) -> Any:
            if node.id in banned_calls:
                nonlocal found
                found = True

    calls: list[ast.Call] = static.getAstNodes(ast.Call)
    for call in calls:
        Visitor().visit(call)

    return found

def has_import(*banned_imports) -> bool:
    imports: list[ast.Import] = static.getAstNodes(ast.Import)
    for imp in imports:
        names = [alias.name for alias in imp.names]
        for name in names:
            if name in banned_imports:
                return True

    imports_from: list[ast.ImportFrom] = static.getAstNodes(ast.ImportFrom)
    for imp in imports_from:
        if imp.module in banned_imports:
            return True

    return False

def has_generators() -> bool:
    return static.getAstNodes(ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp)

def assert_equal(actual, expected) -> bool:
    if actual != expected:
        raise AssertionError(f"verwachtte {expected.__repr__()} maar kreeg {actual.__repr__()}")
    else:
        return True

def assert_return(expected, f, *args):
    actual = f(*args)
    if (
        (expected is None and actual is not None) or
        actual != expected
    ):
        raise AssertionError(f"{f}({', '.join([arg.__repr__() for arg in args])}): "
            f"verwachtte {expected.__repr__()} maar kreeg {actual.__repr__()}")

import re
from typing import Any, Iterable

class RunResult(str):
    def __new__(cls, value: str, **metadata: Any):
        obj = super().__new__(cls, value)
        obj._metadata = dict(metadata)
        return obj

    @property
    def metadata(self) -> dict:
        return self._metadata

    # --- utilities ---------------------------------------------------------
    def with_meta(self, **extra) -> "RunResult":
        """Return a copy with updated/merged metadata."""
        return RunResult(self, **{**self._metadata, **extra})

    def _wrap(self, value, **extra):
        """
        Re-wrap string-like results as RunResult, preserving/merging metadata.
        Recurses into tuples/lists and wraps any str elements.
        """
        meta = {**self._metadata, **extra}
        if isinstance(value, str):
            return RunResult(value, **meta)
        if isinstance(value, tuple):
            return tuple(self._wrap(v, **extra) for v in value)
        if isinstance(value, list):
            return [self._wrap(v, **extra) for v in value]
        return value  # e.g., ints, floats, bytes, None, etc.

    # --- custom helpers ----------------------------------------------------
    def number(self, index: int = 0, pattern: str = r"[-+]?\d*\.?\d+(?:[eE][-+]?\d+)?") -> "RunResult":
        """
        Extract the Nth number substring as a RunResult (preserving metadata).
        Raises ValueError if no such number exists.
        """
        matches = re.findall(pattern, self)
        if index < 0:
            index += len(matches)
        if not (0 <= index < len(matches)):
            # raise ValueError("No matching number found at that index.")
            return self._wrap('')
        return self._wrap(matches[index])

    # --- operations that should obviously preserve subclass ----------------
    def __getitem__(self, key):
        # slicing or single-char access
        return self._wrap(super().__getitem__(key))

    def strip(self, chars: str | None = None) -> "RunResult":
        return self._wrap(super().strip(chars))

    def lstrip(self, chars: str | None = None) -> "RunResult":
        return self._wrap(super().lstrip(chars))

    def rstrip(self, chars: str | None = None) -> "RunResult":
        return self._wrap(super().rstrip(chars))

    def __add__(self, other):
        return self._wrap(super().__add__(other))

    def __radd__(self, other):
        return self._wrap(str(other) + str(self))

    def __mul__(self, n: int):
        return self._wrap(super().__mul__(n))

    def __rmul__(self, n: int):
        return self._wrap(super().__rmul__(n))

    # --- dynamic wrapping for most other str methods -----------------------
    def __getattr__(self, name: str):
        """
        For str methods not explicitly overridden, fetch the corresponding
        function from str and wrap its output if it returns strings/collections.
        """
        attr = getattr(str, name, None)
        if callable(attr):
            def method(*args, **kwargs):
                result = attr(self, *args, **kwargs)
                return self._wrap(result)
            return method
        raise AttributeError(name)

from checkpy.entities import exception

def run(*stdin) -> str:
    stdin = [str(a) for a in stdin]
    try:
        output = outputOf(stdinArgs=stdin, overwriteAttributes = [("__name__", "__main__")])
    except exception.InputError:
        raise AssertionError(
            f"gegeven input: {' ⏎ '.join(stdin)} ⏎\n"
            "het programma bleef hierna toch nog om input vragen")
    return RunResult(
        output,
        stdin=stdin
    )

import re

def assert_output(actual, expected, expected_display=None):
    """
    Compare actual and expected output.

    - If expected_display is None: do direct equality check with expected.
    - If expected_display is given: interpret expected as a regex pattern string,
      and expected_display as the value to show in error messages.
    """
    actual_str = str(actual)
    stdin_str = ' ⏎ '.join(actual.metadata['stdin'])

    # Normalize expected into string form
    if isinstance(expected, re.Pattern):
        match = expected.match(actual_str)
        expected = expected.pattern
    elif expected_display is not None:
        match = re.match(expected, actual_str)
    else:
        match = (actual == expected)

    expected_str = expected_display or expected

    if not match:
        if len(expected_str) + len (actual) > 40:
            raise AssertionError(
                f"gegeven input: {stdin_str} ⏎\n"
                f"verwachte output is:\n"
                f"  {expected_str!r}\n"
                f"maar kreeg:\n"
                f"  {actual!r}"
            )
        else:
            raise AssertionError(
                f"gegeven input: {stdin_str} ⏎\n"
                f"verwachte output is {expected_str!r} maar kreeg {actual!r}"
            )

    return True

import functools

class PrettyCallable:
    def __init__(self, func, expected_name):
        self._func = func
        self._expected_name = expected_name
        self._last_result = None
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        result = self._func(*args, **kwargs)
        self._last_result = result
        return result

    def __repr__(self):
        if self._last_result is not None:
            return f": got {self._last_result!r} but expected {self._expected_name}"
        else:
            return f"<call {self._func.__name__}>"

    __str__ = __repr__

def get_function(name):
    f = getFunction(name)
    return PrettyCallable(f, expected_name=name)

def assert_no_input_output(f):
    if 'print' in f._function.__code__.co_names or 'input' in f._function.__code__.co_names:
        raise AssertionError(
            "deze functie zou geen print of input moeten hebben:\n"
            "meestal moet dat in de if-name-is-main gebeuren")
