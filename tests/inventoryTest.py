from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, mypy_strict, doctest
# forbidden_constructs.disallow_all()

@passed(checkstyle, mypy_strict, doctest)
def test_class():
    """class `Inventory` is aanwezig"""
    Inventory = getModule().Inventory
    # TODO _function
    assert isinstance(Inventory(), Inventory._function)

@passed(test_class)
def test_add_and_get():
    """kan een element met hoeveelheid toevoegen en dan werkt `get_quantity` ook"""
    Inventory = getModule().Inventory
    inv = Inventory()
    inv.add_item("apple", 5)
    assert inv.get_quantity("apple") == 5

@passed(test_class)
def test_default_amount():
    """kan een element toevoegen en `get_quantity` geeft dan de standaardhoeveelheid (1)"""
    Inventory = getModule().Inventory
    inv = Inventory()
    inv.add_item("sword")
    assert inv.get_quantity("sword") == 1

@passed(test_class)
def test_remove():
    """kan een hoeveelheid toevoegen, dan een deel verwijderen en dan klopt `get_quantity`"""
    Inventory = getModule().Inventory
    inv = Inventory()
    inv.add_item("apple", 5)
    inv.remove_item("apple", 2)
    assert inv.get_quantity("apple") == 3

@passed(test_class)
def test_contains():
    """als we een item toevoegen dan kunnen we dat item checken met `in`"""
    Inventory = getModule().Inventory
    inv = Inventory()
    inv.add_item("shield")
    assert "shield" in inv

@passed(test_class)
def test_len():
    """als we twee items toevoegen geeft `len(inventory)` ook echt 2"""
    Inventory = getModule().Inventory
    inv = Inventory()
    inv.add_item("a", 1)
    inv.add_item("b", 2)
    assert len(inv) == 2

@passed(test_class)
def test_list_sorted():
    """als we `list_items` met sorted=True aanroepen krijgen we een lijst op alfabet"""
    Inventory = getModule().Inventory
    inv = Inventory()
    inv.add_item("banana")
    inv.add_item("apple")
    inv.add_item("cherry")
    assert inv.list_items(sorted=True) == ["apple", "banana", "cherry"]

@passed(test_class)
def test_limit():
    """als we een limiet van 1 zetten en dan twee items toevoegen krijgen we een exception"""
    Inventory = getModule().Inventory
    inv = Inventory()
    inv.set_limit(1)
    inv.add_item("apple")
    try:
        inv.add_item("banana")
    except:
        return
    raise AssertionError("geen exception?!")

@passed(test_class)
def test_find_min():
    """de methode `find_by_min_quantity` filtert correct op minimum-hoeveelheid per item"""
    Inventory = getModule().Inventory
    inv = Inventory()
    inv.add_item("apple", 5)
    inv.add_item("pear", 1)
    inv.add_item("banana", 3)
    assert set(inv.find_by_min_quantity(3)) == {"apple", "banana"}
