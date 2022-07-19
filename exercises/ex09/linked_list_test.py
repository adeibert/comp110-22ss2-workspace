"""Tests for linked list utils."""

import pytest
from exercises.ex09.linked_list import Node, last, value_at, max, linkify, scale, is_equal

__author__ = "730460892"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list: Node = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_empty() -> None:
    """Empty list with value_at function should raise a IndexError."""
    with pytest.raises(IndexError):
        value_at(None, 1)


def test_value_at() -> None:
    """Value_at of a Node should return the data of the given index point."""
    linked_list: Node = Node(1, Node(2, Node(3, None)))
    assert value_at(linked_list, 1) == 2


def test_max() -> None:
    """The max funtion should return a linked list's highest data value."""
    linked_list: Node = Node(1, Node(2, Node(3, None)))
    assert max(linked_list) == 3


def test_max_empty() -> None:
    """Empty list with max function should raise a ValueError."""
    with pytest.raises(ValueError):
        max(None)


def test_linkify() -> None:
    """Given a linked list the linkify function should produce the data values."""
    list: list[int] = [1, 2, 3]
    lists: Node = Node(1, Node(2, Node(3, None)))
    assert is_equal(linkify(list), lists) is True


def test_linkify_empty() -> None:
    """Linkify of an empty list should return None."""
    index: list[int] = []
    assert linkify(index) is None


def test_scale() -> None:
    """Scale of a non-empty list should return the data values multiplied by the factor."""
    list: Node = Node(1, Node(2, Node(3, None)))
    lists: Node = Node(2, Node(4, Node(6, None)))
    factor: int = 2
    assert is_equal(scale(list, factor), lists) is True


def test_scale_zero() -> None:
    """Scale with factor 0 returns all 0 data values."""
    linked_list: Node = Node(1, Node(2, Node(3, None)))
    factor: int = 0
    lists: Node = Node(0, Node(0, Node(0, None)))
    assert is_equal(scale(linked_list, factor), lists) is True