"""Practice for 'list' utility functions."""

__author__ = "730460892"


def only_evens(list_1: list[int]) -> list[int]:
    """Returning only even values from an int list."""
    list_1: list[int]
    i: int = 0
    while i < len(list_1):
        num: int = list_1[i]
        if num % 2 == 0:
            i += 1
        else:
            list_1.pop(i)
            i += 1
    return list_1


def is_equal(x: list[int], y: list[int]) -> bool:
    """Evaluating if two lists are the same as eachother."""
    i: int = 0
    match: bool = True
    if len(x) != len(y):
        match = False
    while i < len(x) and match == True:
        if x[i] == y[i]:
            i += 1
        else:
            match = False
    return match


def sub(a_list: list[int], index: int, end_index: int):
    """Returning a certain set of values from a list between 2 specific indexes."""
    b_list: list[int] = a_list[index]
    index += 1
    while index <= end_index: 
        b_list = b_list + a_list[index] 
        index += 1
    return a_list
