from enum import Enum
import random

from ascii.ascii_characters import ascii_characters
from ascii.words import long_words, medium_words, short_words


class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    SUPER_HARD = 4
    IMPOSSIBLE = 5

#TODO: Figure out keylists for each difficulty.
def get_keylist(difficulty) -> list:
    match difficulty:
        case Difficulty.EASY:
            return short_words
        case Difficulty.MEDIUM:
            return short_words + medium_words
        case Difficulty.HARD:
            return medium_words
        case Difficulty.SUPER_HARD:
            return medium_words + long_words
        case Difficulty.IMPOSSIBLE:
            return long_words
        case _:
            raise Exception("Error getting keylist: No valid difficulty selected.")

def select_random_key(difficulty) -> str:
    keylist = get_keylist(difficulty)
    return random.choice(keylist)

def key_to_art(key) -> str:
    return ascii_characters[key]

def select_difficulty() -> Enum:
    print("Select difficulty:")
    print(" [1] Easy")
    print(" [2] Medium")
    print(" [3] Hard")
    print(" [4] Super Hard")
    print(" [5] Impossible")

    difficulty = None
    while difficulty is None:
        user_input = input(">>> ").strip()
        try:
            difficulty = Difficulty(int(user_input))
        except Exception as e:
            print(f"{e}. Enter a valid number[1-5] without brackets and press ENTER.")
    return difficulty
