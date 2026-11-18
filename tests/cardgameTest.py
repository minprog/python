from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, mypy_strict, doctest

import inspect

SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS_SET = set(SUITS)
VALUES_SET = set(VALUES)


def get_class(name):
    """Haal een class op uit de module van de student."""
    module = getModule()
    if not hasattr(module, name):
        raise AssertionError(f"class `{name}` is niet aanwezig")

    cls = getattr(module, name)

    # checkpy wraps everything callable in a Function object, unwrap it
    cls = getattr(cls, "_function", cls)

    if not isinstance(cls, type):
        raise AssertionError(f"`{name}` is geen class")
    return cls


def assert_attributes(obj, attributes):
    """Controleer of elk gevraagd attribuut aanwezig is in het object."""
    for attribute in attributes:
        if not hasattr(obj, attribute):
            raise AssertionError(
                f"class `{type(obj).__name__}` heeft geen attribuut "
                f"`{attribute}`")
    return True


def assert_method(cls, method):
    """Controleer of de methode bestaat in de class."""
    if not hasattr(cls, method) or not callable(getattr(cls, method)):
        raise AssertionError(
            f"methode `{method}()` is niet aanwezig in class `{cls.__name__}`")
    return True


def assert_parameters(cls, method, required):
    """Controleer of de methode precies de gevraagde parameters heeft."""
    args = inspect.getfullargspec(getattr(cls, method)).args

    if len(args) != len(required):
        raise AssertionError(
            f"methode `{method}()` in class `{cls.__name__}` heeft "
            f"{len(args)} parameter(s), verwachtte {len(required)}")

    for arg in required:
        if arg not in args:
            raise AssertionError(
                f"verwachtte dat methode `{method}()` in class "
                f"`{cls.__name__}` een parameter `{arg}` heeft")
    return True


def assert_deck_valid(deck):
    """Controleer of de deck 52 verschillende, geldige kaarten bevat."""
    Card = get_class("Card")
    seen = set()

    if len(deck._cards) != 52:
        raise AssertionError(
            f"de deck bevat {len(deck._cards)} kaarten, verwachtte 52")

    for card in deck._cards:
        if not isinstance(card, Card):
            raise AssertionError(
                f"de kaarten in de deck zijn geen objecten van class `Card`, "
                f"maar van `{type(card).__name__}`")

        assert_attributes(card, ["suit", "value"])

        if card.suit + card.value in seen:
            raise AssertionError(
                f"de kaart {card.value} of {card.suit} zit minstens "
                f"twee keer in de deck")
        seen.add(card.suit + card.value)

        if card.value not in VALUES_SET or card.suit not in SUITS_SET:
            raise AssertionError(
                f"de deck bevat een ongeldige kaart: {card.value} "
                f"of {card.suit}")
    return True


@passed(checkstyle, mypy_strict, doctest)
def test_card_class():
    """class `Card` is aanwezig"""
    assert get_class("Card")


@passed(test_card_class)
def test_card_initializer():
    """class `Card` kan correct geinitialiseerd worden"""
    Card = get_class("Card")
    assert assert_method(Card, "__init__")
    assert assert_parameters(Card, "__init__", ["self", "suit", "value"])

    for suit in SUITS:
        for value in VALUES:
            card = Card(suit=suit, value=value)
            assert assert_attributes(card, ["suit", "value"])

            if card.suit != suit:
                raise AssertionError(
                    f"class `Card` heeft na initialisatie suit "
                    f"{card.suit!r}, verwachtte {suit!r}")
            if card.value != value:
                raise AssertionError(
                    f"class `Card` heeft na initialisatie value "
                    f"{card.value!r}, verwachtte {value!r}")


@passed(test_card_initializer)
def test_card_description():
    """methode `description()` in class `Card` geeft de juiste output"""
    Card = get_class("Card")
    assert assert_method(Card, "description")

    for suit in SUITS:
        for value in VALUES:
            card = Card(suit=suit, value=value)
            description = card.description().strip()

            if description != f"{value} of {suit}":
                raise AssertionError(
                    f"met suit {suit!r} en value {value!r} geeft "
                    f"`description()` {description!r}, verwachtte "
                    f"{f'{value} of {suit}'!r}")


@passed(test_card_description)
def test_deck_initializer():
    """class `Deck` is aanwezig en kan correct geinitialiseerd worden"""
    Deck = get_class("Deck")
    assert assert_method(Deck, "__init__")
    assert assert_parameters(Deck, "__init__", ["self"])

    deck = Deck()
    assert assert_attributes(deck, ["_suits", "_values"])

    if not all(suit in SUITS_SET for suit in deck._suits):
        raise AssertionError(
            "verwachtte dat `deck._suits` na initialisatie alle mogelijke "
            "suits bevat")
    if not all(value in VALUES_SET for value in deck._values):
        raise AssertionError(
            "verwachtte dat `deck._values` na initialisatie alle mogelijke "
            "values bevat")


@passed(test_deck_initializer)
def test_instantiate_cards():
    """de kaarten worden aangemaakt in de deck"""
    deck = get_class("Deck")()
    assert assert_attributes(deck, ["_cards"])
    assert assert_deck_valid(deck)


@passed(test_instantiate_cards)
def test_shuffle():
    """deck verandert en blijft compleet na `shuffle()`"""
    Deck = get_class("Deck")
    deck = Deck()

    assert assert_method(Deck, "shuffle")
    assert assert_parameters(Deck, "shuffle", ["self"])

    original = [card.value + card.suit for card in deck._cards]
    deck.shuffle()
    shuffled = [card.value + card.suit for card in deck._cards]

    if original == shuffled:
        raise AssertionError("deck is niet veranderd na `shuffle()`")

    assert assert_deck_valid(deck)


@passed(test_shuffle)
def test_deal():
    """`deal()` geeft de bovenste kaart terug en haalt die uit de deck"""
    Deck = get_class("Deck")
    deck = Deck()

    assert assert_method(Deck, "deal")
    assert assert_parameters(Deck, "deal", ["self"])

    deck.shuffle()

    for _ in range(52):
        start_len = len(deck._cards)
        top_card = deck._cards[-1]

        card = deck.deal()

        if len(deck._cards) != start_len - 1:
            raise AssertionError(
                f"`deal()` veranderde het aantal kaarten van {start_len} "
                f"naar {len(deck._cards)}, verwachtte {start_len - 1}")

        if card is not top_card:
            raise AssertionError(
                f"`deal()` gaf {card.value} of {card.suit} terug, maar de "
                f"bovenste kaart was {top_card.value} of {top_card.suit}")

        if deck._cards and deck._cards[-1] is top_card:
            raise AssertionError(
                "`deal()` haalde een andere kaart dan de bovenste kaart "
                "uit de deck")
