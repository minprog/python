from checkpy import *
# from _basics import *
from _pyprog_tools import *

getClass = getFunction

import math

@test()
def has_classes():
    """De benodigde klassen `Quare`, `Rectangle`, `Circle` en `Shape` zijn aanwezig"""
    assert "class Square" in static.getSource()
    assert "class Rectangle" in static.getSource()
    assert "class Circle" in static.getSource()
    assert "class Shape" in static.getSource()

@passed(has_classes)
def test_square_methods():
    """De klasse `Square` heeft correcte implementaties van de gevraagde methoden"""
    Square = getClass("Square")
    
    try:
        test_square = Square(4)
    except:
        raise AssertionError("Square(4) aanmaken met één argument moet mogelijk zijn")
    
    assert hasattr(test_square, "area"), "De methode `area` ontbreekt in de klasse Rectangle"
    assert test_square.area() == 4 * 4, "De methode `area` van `Rectangle` werkt niet correct"
    # assert not hasattr(test_square, "__lt__"), "De methode `__lt__` mag niet gedefinieerd zijn in Square"
    assert hasattr(test_square, "__repr__"), "De methode `__repr__` moet gedefinieerd zijn voor Square"
    
@passed(has_classes)
def test_rectangle_methods():
    """De klasse `Rectangle` heeft correcte implementaties van de gevraagde methoden"""
    Rectangle = getClass("Rectangle")
    
    try:
        test_rectangle = Rectangle(4, 6)
    except:
        raise AssertionError("Rectangle(4, 6) aanmaken met twee argumenten moet mogelijk zijn")
    
    assert hasattr(test_rectangle, "area"), "De methode `area` ontbreekt in de klasse Rectangle"
    assert test_rectangle.area() == 4 * 6, "De methode `area` van Rectangle werkt niet correct"
    # assert not hasattr(test_rectangle, "__lt__"), "De methode `__lt__` mag niet gedefinieerd zijn in Rectangle"
    assert hasattr(test_rectangle, "__repr__"), "De methode `__repr__` moet gedefinieerd zijn voor Rectangle"
    
@passed(has_classes)
def test_circle_methods():
    """De klasse `Circle` heeft correcte implementaties van de gevraagde methoden"""
    Circle = getClass("Circle")
    
    try:
        test_circle = Circle(5)
    except:
        raise AssertionError("Circle(5) aanmaken met één argument moet mogelijk zijn")
    
    assert hasattr(test_circle, "area"), "De methode `area` ontbreekt in de klasse Circle"
    assert math.isclose(test_circle.area(), math.pi * 5 ** 2), "De methode `area` van `Circle` werkt niet correct"
    # assert not hasattr(test_circle, "__lt__"), "De methode `__lt__` mag niet gedefinieerd zijn in Square"
    assert hasattr(test_circle, "__repr__"), "De methode `__repr__` moet gedefinieerd zijn voor Circle"
    
@passed(has_classes)
def test_shape_methods():
    """De klasse `Shape` heeft lege implementaties van de gevraagde methoden"""
    Shape = getClass("Shape")
    
    try:
        test_shape = Shape()
    except:
        raise AssertionError("Shape() aanmaken met nul argumenten moet mogelijk zijn")
    
    assert hasattr(test_shape, "__lt__"), "De methode `__lt__` ontbreekt in de klasse Shape"
    assert hasattr(test_shape, "area"), "De methode `area` ontbreekt in de klasse Shape"
    assert test_shape.area() == None, "De methode `area` van `Rectangle` moet None returnen"
    # assert not hasattr(test_shape, "__lt__"), "De methode `__repr__` mag niet gedefinieerd zijn in Shape"
    
@passed(has_classes)
def test_common_methods():
    """Beide klassen ondersteunen correcte implementaties van gemeenschappelijke methoden"""
    Circle = getClass("Circle")
    Rectangle = getClass("Rectangle")
    
    test_circle = Circle(5)
    test_rectangle = Rectangle(4, 6)
    
    assert hasattr(test_circle, "__repr__"), "De methode `__repr__` ontbreekt in de klasse Circle"
    assert isinstance(test_circle.__repr__(), str), "De methode `__repr__` van `Circle` geeft geen string terug"
    
    assert hasattr(test_rectangle, "__repr__"), "De methode `__repr__` ontbreekt in de klasse Rectangle"
    assert isinstance(test_rectangle.__repr__(), str), "De methode `__repr__` van `Rectangle` geeft geen string terug"

@passed(has_classes)
def test_shape_methods():
    """De klasse `Shape` heeft implementaties van alle vergelijkings-operators"""
    Shape = getClass("Shape")
    
    test_shape = Shape()
    
    assert "def __le__" in static.getSource(), "__le__ moet gedefinieerd zijn in Shape"
    assert "def __eq__" in static.getSource(), "__le__ moet gedefinieerd zijn in Shape"
    assert "def __ne__" in static.getSource(), "__le__ moet gedefinieerd zijn in Shape"
    assert "def __gt__" in static.getSource(), "__le__ moet gedefinieerd zijn in Shape"
    assert "def __ge__" in static.getSource(), "__le__ moet gedefinieerd zijn in Shape"
    
@passed(test_circle_methods)
@passed(test_rectangle_methods)
def test_interaction():
    """De klassen `Circle` en `Rectangle` functioneren samen zoals beschreven in de opdracht"""
    Circle = getClass("Circle")
    Rectangle = getClass("Rectangle")
    
    c1 = Circle(5)
    r1 = Rectangle(4, 6)
    
    assert c1.area() > r1.area(), "De oppervlakte van Circle met radius 5 is groter dan Rectangle met dimensies 4x6"
