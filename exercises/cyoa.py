"""90s Movie Trivia."""

__author__ = "730460892"


points: int = 100
player: str = input("Hi! Welcome to 90s movie trivia! What is your name? ")


def main() -> None:
    """Running the greet and giving path options."""
    greet()
    global points
    stay: bool = True
    while stay == True:
        path: int = int(input("To see what happens next choose a path 1-3: "))
        if path == 1:
            game_over()
            stay = False
        if path == 2:
            path_two(points)
            print(f"Your adventure points: {points}")
        if path == 3: 
            path_three(points)
            print(f"Your adventure points: {points}")
    print("Thanks for playing!")


def greet() -> None:
    """Welcome to the player."""
    print(f"Welcome {player}!")
    print("Oh no! You were sucked into your TV and transported to Hollywood in the 90s! To get back home test how much you know about the 90s movie scene and be sure to ansewr in only lowercase letters!")
    print("Every wrong answer deducts 10 adventure points from your starting 100.")
    star_face: str = "\U0001F929"
    money_face: str = "\U0001F911"
    sleepy_face: str = "\U0001F62A"
    from random import randint
    profile: int = randint(1, 3)
    if profile == 1:
        print(f"Your profile:{star_face}")
    if profile == 2:
        print(f"Your profile:{money_face}")
    if profile == 3:
        print(f"Your profile:{sleepy_face}")


def game_over() -> None:
    """Closing out the game."""
    global points
    print(f"phew! you were able to make it home by just wishing upon a star. Game over. Your total adventrue points: {points}")


def path_two(qs: int) -> int:
    """Family film trivia path."""
    global points
    print("You are now on the set of some classic family films. To find your way out answer the next few questions.")
    points = qs
    q1: str = input("In 'The Adams Family' what was the name of the daughter who bullied her brother? ")
    while q1 != str("wednesday"):
        q1 = input("Not quite! 10 points lost. Try again: ")
        points = points - 10
    if q1 == "wednesday":
        print("Yes! now heres the next obstical.")
    q2: str = input("Next challenge: What movie with Robin Williams had a game that turned a boy into a monkey? ")
    while q2 != str("jumanji"):
        q2 = input("Not quite! 10 points lost. Try again: ")
        points = points - 10
    if q2 == str("jumanji"):
        print("Yes! on to the next obsitcal.")
    return points


def path_three(qt: int) -> int:
    """Family sports movie trivia path."""
    global points
    points = qt
    print("You are now on the set of some classic sport films. To find your way out answer the next few questions.")
    q1: str = input("In 'The Sandlot' what was the name of the dog who they had to get the ball back from? ")
    while q1 != "the beast": 
        q1 = input("Not quite! 10 points lost. Try again: ")
        points = points - 10
    if q1 == "the beast":
        print("Yes! now heres the next challenge.")
    q2: str = input("Next challenge: In 'Rudy' what school did the main character try to play football for? ")
    while q2 != str("notre dame"):
        q2 = input("Not quite! 10 points lost. Try again: ")
        points = points - 10
    if q2 == "notre dame":
        print("Yes! on to the next obsitcal.")
    return points


if __name__ == "__main__":
    main()
    