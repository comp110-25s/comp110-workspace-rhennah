"""Coding the Wordle!"""

__author__: str = "730470881"


def contains_char(word: str, character: str) -> bool:
    """Checking to see if the character is contained in the secret word"""
    assert len(character) == 1, f"len('{character}') is not 1"

    # Starting w/ the first letter, it's checking to see if the character matches
    # After the checking, it will move on until is has checked all characters
    index = 0
    while index < len(word):
        if word[index] == character:
            return True
        index += 1

    return False


def emojified(guess: str, secret: str) -> str:
    """Convert a guess into emoji boxes based on the secret word"""
    assert len(guess) == len(secret), "Guess must be same length as secret"

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    result = ""

    # Again, starting at an index of 0, for each index of the guess it will:
    # Determine, does the index letter of guess match the index of the secret? Green!
    # Does the index letter of guess appear within secret? Yellow!
    # Does the index letter not show up at all within secret? White!
    # And it will start with the first letter, checking all three conditions,
    # move to the second letter to do this, and so on...
    i = 0
    while i < len(guess):
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1

    return result


def input_guess(expected_length: int) -> str:
    """Starting with setting the expected length &
    then asking for a guess to assure the length is the same!"""
    while True:
        guess = input(f"Enter a {expected_length} character word: ")
        if len(guess) == expected_length:
            return guess
        else:
            print(f"That wasn't {expected_length} chars! Try again:")


def main(secret: str) -> None:
    """The entrypoint of the program and the main game loop"""
    turns_left = 6
    turns_taken = 0
    won = False

    while turns_taken < turns_left and not won:
        turns_taken += 1  # To assure we are continuing to increase # of turns until 6
        print(f"=== Turn {turns_taken}/6 ===")

        guess = input_guess(len(secret))  # Checking to see if correct length

        emoji_result = emojified(guess, secret)
        print(emoji_result)

        if guess == secret:
            won = True

    if won:
        print(f"You won in {turns_taken}/6 turns!")
    else:
        print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
