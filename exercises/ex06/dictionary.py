"""Exercise 06 dictionaries to be tested."""

__author__ = "730460892"


def invert(my_dictionary: dict[str, str]) -> dict[str, str]:
    my_inv_dictionary: dict[str, str] = {}
    for word in my_dictionary:
        for key in my_inv_dictionary:
            if my_dictionary[word] == key:
                raise KeyError("Value repeated -> Invalid as key.")
        my_inv_dictionary[my_dictionary[word]] = word
    return my_inv_dictionary



def favorite_color(favs: dict[str, str]) -> str:
    tally_dict: dict[str, int] = {}
    highest_value: str = "nothing"
    for word in favs:
        tally: int = 1
        for key in tally_dict:
            if favs[word] == key:
                tally += 1
        tally_dict[favs[word]] = tally 
    highest_value = max(tally_dict, key=tally_dict.get)
    return highest_value
        

def count(values: list[str]) -> dict[str, int]:
    counts: dict[str, int] = {}
    times_present: int = 1
    for value in values:
        if value in counts:
            times_present += 1
            counts[value] = times_present
        else:
            counts[value] = times_present
    return counts

