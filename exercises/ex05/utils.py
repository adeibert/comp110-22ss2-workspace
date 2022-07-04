"""Practice for 'list' utility functions."""

__author__ = "730460892"

def only_evens(list_1: list[int]) -> list[int]:
    list_1: list[int] = [1, 2, 3]
    i: int = 0
    while i > len(list_1):
        num: int = list_1[i]
        if num % 2 == 0:
            i += 1
        else:
            list_1.pop(num)
            i += 1
    print(list_1)


