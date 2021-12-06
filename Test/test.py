
"""
this modul for testing sum,product and sequer for linkedlist values
"""
from Pythonisms.pythonisms import Node, LinkedList, MathThings
import pytest


def test_insert():
    # Arrange
    ll = LinkedList()
    ll.insert(5)
    ll.insert(2)
    ll.insert(25)
    expected = 25
    expected_ll = "{25}->{2}->{5}"
    # Actual
    actual = ll.head.data
    actual_ll = str(ll)
    # Assert
    assert actual == expected
    assert actual_ll == expected_ll


def test_ll_from_collection():
    ll = LinkedList([1, 2])
    expected = "{1}->{2}"
    actual = str(ll)
    assert actual == expected


def test_iteration():
    ll = LinkedList([1, 2])
    expected = [1, 2]
    for index, actual_item in enumerate(ll):
        assert actual_item == expected[index]


def test_indexing():
    ll = LinkedList([1, 2])
    expected_0 = 1
    expected_1 = 2
    actual_0 = ll[0]
    actual_1 = ll[1]
    assert actual_0 == expected_0
    assert actual_1 == expected_1
    with pytest.raises(IndexError, match="Index out of range"):
        actual = ll[2]


def test_product():
    # Arrange
    expected = 40
    # Act
    ll = LinkedList([1, 5, 2, 4])
    actual = ll.find_product()
    # Assert
    assert actual == expected


def test_list():
    l1 = LinkedList()
    l1.insert(2)
    l1.insert(1)
    l1.insert(3)
    l1.insert(1)
    expected = [1, 9, 1, 4]
    actual = l1.linked_list_squared()
    assert actual == expected
