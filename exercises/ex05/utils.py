"""Practice for 'list' utility functions."""

__author__ = "730460892"

def only_evens(list_1: list[int]) -> list[int]:
    list_1: list[int] = [1, 2, 3]
    i: int = 0
    while i < len(list_1):
        num: int = list_1[i]
        if num % 2 == 0:
            i += 1
        else:
            list_1.pop(num)
            i += 1
    print(list_1)


def is_equal(x: list[int], y: list[int]) -> bool:
    i: int = 0
    match: bool = True
    while i < len(x) and match == True:
        if x[i] == y[i]:
            i += 1
        else:
            match = False
            print(match)
    print(True)


def sub(a_list: list[int], index: int, end_index: int):
    a_list = a_list[index]
    index += 1
    while index <= end_index: 
        a_list = a_list + a_list[index]
        index += 1
    print(a_list)
