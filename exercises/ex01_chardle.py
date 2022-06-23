"""Input, Variables, and Conditionals Practice."""


__author__ = "730460892"


chosen_word: str = input("Enter a 5-character word: ")
if len(chosen_word) != 5:
    print("Error: Word must contain 5 characters")
else:
    single_letter: str = input("Enter a single character: ")
    if len(single_letter) != 1:
        print("Character must be a single character.")
    else:
        letter_amount: int = 0
        print("Searching for " + single_letter + " in " + chosen_word)

        if single_letter == str(chosen_word)[0]:
            print(single_letter + " found at index 0")
            letter_amount = letter_amount + 1
        if single_letter == chosen_word[1]:
            print(single_letter + " found at index 1")
            letter_amount = letter_amount + 1
        if single_letter == chosen_word[2]:
            print(single_letter + " found at index 2")
            letter_amount = letter_amount + 1
        if single_letter == chosen_word[3]:
            print(single_letter + " found at index 3")
            letter_amount = letter_amount + 1
        if single_letter == chosen_word[4]:
            print(single_letter + " found at index 4")
            letter_amount = letter_amount + 1
        if letter_amount >= 1:
            print(str(letter_amount) + " instances of " + single_letter + " found in " + chosen_word)
        else: 
            print("No instances of " + single_letter + " found in " + chosen_word)