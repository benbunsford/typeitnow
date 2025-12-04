from user_prompt import select_difficulty, select_random_key, key_to_art
from music import MusicPlayer
from game_over import game_over
import sys
from inputimeout import inputimeout,TimeoutOccurred
import time

def main():
    print("Welcome to type-it! Press the correct key/button when prompted to score.\n")

    difficulty = select_difficulty()

    print("3...")
    time.sleep(.25)
    print("2...")
    time.sleep(.25)
    print("1...")
    time.sleep(.25)

    player = MusicPlayer()
    player.play_async()
    print(".\n" * 60)
    print(
"""
---------------------------------------
            !!! START !!!
---------------------------------------
"""
    )
    score = 0
    timer_length = 6
    while True:
        key = select_random_key(difficulty)
        ascii_key = key_to_art(key)
        print(ascii_key)
        print("..................................")
        print(f"Timer: {round(timer_length, 2)}s")

        try:
            pressed_key = inputimeout(prompt='', timeout=timer_length)
        except TimeoutOccurred:
            pressed_key = ''

        if pressed_key == key:
            score += 1
            player.speed_up()
            if timer_length > 1.5:
                timer_length -= .05
        elif pressed_key == '':
            pressed_key = "NOTHING"
            game_over(key, pressed_key, score)
            player.stop()
            sys.exit()
        else:
            game_over(key, pressed_key, score)
            player.stop()
            sys.exit()

if __name__ == "__main__":
    main()
