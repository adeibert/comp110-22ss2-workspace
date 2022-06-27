"""Six shot wordle."""

__author__ = "730460892"


def contains_char(word: str, char: str) -> bool:
    """If a guessed character matches any in the assigned word."""
    assert len(char) == 1
    i: int = 0
    present: bool = False
    while present is False and i < len(word):
        if word[i] == char:
            present = True
        else:
            i = i + 1
    if present is True:
        return True
    else:
        return False

def emojified(guess: str, word: str) -> str:
    """Stating string of emojis to code the secret word."""
    assert len(guess) == len(word)
    codified: str = ""
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    e: int = 0
    while e < len(word):
        if guess[e] == word[e]:
            codified = codified + green_box 
        else:
            if contains_char(word, guess[e]) is True:
                codified = codified + yellow_box
            else:
                codified = codified + white_box
        e = e + 1
    return codified

def  input_guess(chars: int) -> int:
    """Matching character length of guess and secret word."""
    guess: str = input(f"Enter a {chars} character word: ")
    while len(guess) != chars:
        guess = input(f"That wasn't {chars} chars! Try again: ")
    return guess 

def  main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    success: bool = False
    game_guess: str = ""
    while (turns <= 6) and success is False: 
        print(f"=== Turn {turns}/6 ===")
        game_guess = (input_guess(len(secret_word)))
        print(emojified(game_guess, secret_word))
        if game_guess == secret_word:
            success = True
            print(f"You won in {turns}/6 turns!")
        else:
            turns = turns + 1
    if turns > 6 and success is False:
        print("x/6 - Sorry, try again tomorrow!")
    if __name__ == "__main__":
        main()
