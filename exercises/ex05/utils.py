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
    b_list: list[int] = []
    if index < 0:
        index = 0
    if end_index > len(a_list):
        end_index = (len(a_list))
    if len(a_list) == 0 or len(a_list) <= index or end_index <= 0:
        return []
    b_list.append(a_list[index])
    index += 1
    while index < end_index: 
        b_list.append(a_list[index]) 
        index += 1
    return b_list
