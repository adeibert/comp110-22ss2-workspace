"""Testing functions in the dictionary file."""

__author__ = "730460892"


from exercises.ex06.dictionary import invert, favorite_color, count
import pytest


with pytest.raises(KeyError):
    """Checking for Key Error while running invert function"""
    my_dictionary = {"ava": "soph", "emi": "fresh", "bar": "jun"}
    invert(my_dictionary)


def test_empty_list() -> None:
    """Testing to see if an empty list would return an empty list."""
    my_dictionary = {}
    assert invert(my_dictionary) == {}


def test_if_given_list_returns_inverted() -> None:
    """Testing if a simple list would return with keys and values inverted."""
    my_dictionary = {"a": "s", "e": "f", "b": "j"}
    assert invert(my_dictionary) == {"s": "a", "f": "e", "j": "b"}


def test_for_empty_dictionary() -> None:
    """Testing to see if an empty dictionary would return an empty string value."""
    favs = {}
    assert favorite_color(favs) == {}


def test_for_two_same_highest_values() -> None:
    """Testing if two of the same highest value would return the first key."""
    favs = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Ella": "yellow"}
    assert favorite_color(favs) == 'yellow'


def test_if_returns_highest_value_in_dict() -> None:
    """Testing to see if it will return the value repeated the most in the dictionary."""
    favs = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(favs) == 'blue'


def test_amount_each_str_is_listed() -> None:
    """Testing if a simple list would return with keys and values of the amount of times each string is in the list."""
    values = ['a', 'b', 'c', 'a']
    assert count(values) == {'a': 2, 'b': 1, 'c': 1}


def test_if_given_empty_list() -> None:
    """Testing to see if an empty list would return an empty dict."""
    values = []
    assert count(values) == {}


def test_3() -> None:
    """Testing if a list of only one repeated string records how many times its listed."""
    values = ['a', 'a', 'a', 'a']
    assert count(values) == {'a': 4}