from checkpy import *
from _pyprog_tools import *

from _python_checks import checkstyle, mypy_strict, doctest
# forbidden_constructs.disallow_all()

@passed(checkstyle, mypy_strict, doctest)
def test_phonebook():
    """class `Phonebook` werkt correct"""
    Phonebook = getModule().Phonebook

    # initializer
    p1 = Phonebook()
    assert p1._contacts == dict(), "na aanmaken van een Phonebook moet deze een lege dict _contacts bevatten"

    p2 = Phonebook({'Martijn': '5235', 'Rein': '0611'})
    assert p2._contacts is not None
    assert p2._contacts != getattr(Phonebook({'Martijn': '5235'}), '_contacts'), "contact_list moet gekopieerd worden"
    assert str(p2._contacts['Martijn']) == '5235', "na aanmaken van Phonebook met dict moet deze informatie opgeslagen zijn in de _contacts dict"

    # add_contact
    p1.add_contact('Martijn', '5235')
    assert p1._contacts['Martijn'] == '5235', "na aanroep van add_contact moet de _contacts dict een extra nummer bevatten"

    raised = False
    try:
        p1.add_contact('Martijn', 'XXXX')
    except KeyError:
        raised = True
    assert raised, "add_contact moet KeyError geven bij duplicate key"

    # get_number
    assert p1.get_number('Martijn') == '5235', "get_number moet het nummer retourneren"
    assert p1.get_number('Onbekend') is None, "get_number moet None retourneren voor onbekende naam"

    # remove_contact
    p1.remove_contact('Martijn')
    assert 'Martijn' not in p1._contacts, "remove_contact moet het item verwijderen"
    p1.remove_contact('Martijn')  # mag geen error geven

    # update_number
    p1.add_contact('A', '1')
    p1.update_number('A', '2')
    assert p1._contacts['A'] == '2', "update_number moet het nummer bijwerken"

    # list_contacts
    p3 = Phonebook({'b': '2', 'a': '1', 'c': '3'})
    assert p3.list_contacts() == ['a', 'b', 'c'], "list_contacts moet gesorteerde lijst van namen geven"

    # search_by_prefix
    assert sorted(p3.search_by_prefix('a')) == ['a'], "search_by_prefix moet namen vinden die beginnen met prefix"

    # reverse_lookup
    assert sorted(p3.reverse_lookup('2')) == ['b'], "reverse_lookup moet namen vinden bij een nummer"

    # count_contacts
    assert p3.count_contacts() == 3, "count_contacts moet lengte van telefoonboek geven"

    # to_dict
    d = p3.to_dict()
    assert d == p3._contacts, "to_dict moet kopie van interne dict geven"
    d['x'] = 'y'
    assert 'x' not in p3._contacts, "wijzigingen in kopie mogen origineel niet beïnvloeden"

    # merge
    p4 = Phonebook({'x': '9'})
    p3.merge(p4)
    assert 'x' in p3._contacts, "merge moet contacten toevoegen"
    assert p3._contacts['x'] == '9', "merge moet correcte nummers overnemen"
