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
            if n.func.attr in ['replace', 'find']:
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
        for name in imp.names:
            if name in banned_imports:
                return True

    return False

def has_generators() -> bool:
    return static.getAstNodes(ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp)

def assert_equal(actual, expected) -> bool:
    if actual != expected:
        raise AssertionError(f"verwachtte {expected.__repr__()} maar kreeg {actual.__repr__()}")
    else:
        return True

def assert_call(expected, f, *args):
    actual = f(*args)
    if (
        (expected is None and actual is not None) or
        actual != expected
    ):
        raise AssertionError(f"{f}({','.join([arg.__repr__() for arg in args])}): "
            f"verwachtte {expected.__repr__()} maar kreeg {actual.__repr__()}")

def run(*args) -> str:
    return outputOf(stdinArgs=args, overwriteAttributes = [("__name__", "__main__")])
