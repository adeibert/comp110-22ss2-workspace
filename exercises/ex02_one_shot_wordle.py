"""One Guess Wordle Exercise."""

__author__ = "730460892"


secret_word: str = "python"
word_guess: str = input(f"What is your {len(secret_word)}-letter guess? ")
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"
i: int = 0
box_emoji: str = ""

while len(word_guess) != len(secret_word):
    word_guess = input(f"That was not {len(secret_word)} letters! Try again: ")

while i < len(secret_word):
    """Checking if current index of guess matches same index of secret word."""
    if word_guess[i] == secret_word[i]:
        box_emoji = box_emoji + green_box
    else:
        track: bool = False
        e: int = 0
        while (track == False) and e < len(secret_word):
            """Checking current index of guess with each index of secret word."""
            if word_guess[i] == secret_word[e]:
                track = True 
            else: 
                e = e + 1
        if track == True:
            box_emoji = box_emoji + yellow_box
        else:
            box_emoji = box_emoji + white_box
    i = i + 1
print(box_emoji)
if word_guess == secret_word:
    print("Whoo! You got it!")
else:
    print("Not quite. Play again soon!")
